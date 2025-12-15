"""
P-Mark-III - Main Application
Version: 1.0.2
Phase: P-1.2 + P-1.3
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'p-mark-iii-secret-key-2503-proftvv')
app.config['SESSION_PERMANENT'] = False

# Default user credentials
DEFAULT_USERNAME = os.getenv('DEFAULT_USERNAME', 'proftvv')
DEFAULT_PASSWORD = os.getenv('DEFAULT_PASSWORD', '2503')
DEFAULT_PASSWORD_HASH = generate_password_hash(DEFAULT_PASSWORD)

# Simple in-memory user database (will be replaced with proper DB in P-2)
USERS = {
    DEFAULT_USERNAME: DEFAULT_PASSWORD_HASH
}


def login_required(f):
    """Decorator to protect routes that require authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Lütfen önce giriş yapın.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    """Home page - redirects to login if not authenticated"""
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and authentication handler"""
    if 'username' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember') == 'on'
        
        # Validate credentials
        if username in USERS and check_password_hash(USERS[username], password):
            session['username'] = username
            session.permanent = remember
            flash(f'Hoş geldin, {username}!', 'success')
            
            # Log successful login
            log_action('LOGIN', f'User {username} logged in successfully')
            
            return redirect(url_for('dashboard'))
        else:
            flash('Kullanıcı adı veya şifre hatalı!', 'error')
            log_action('LOGIN_FAILED', f'Failed login attempt for user: {username}')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """Logout handler"""
    username = session.get('username', 'Unknown')
    session.pop('username', None)
    flash('Başarıyla çıkış yaptınız.', 'info')
    log_action('LOGOUT', f'User {username} logged out')
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard - will contain search functionality"""
    username = session.get('username', 'User')
    return render_template('dashboard.html', username=username)


def log_action(action_type, message):
    """Log actions to debug log"""
    from datetime import datetime
    log_file = 'debug/debug.log'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {action_type}: {message}\n"
    
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Error writing to log: {e}")


@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'True') == 'True'
    
    print(f"""
    ╔══════════════════════════════════════════╗
    ║         P-Mark-III v1.0.2               ║
    ║     Business Intelligence System         ║
    ╚══════════════════════════════════════════╝
    
    🚀 Server starting...
    🌐 URL: http://{host}:{port}
    👤 Default User: {DEFAULT_USERNAME}
    🔑 Default Pass: {DEFAULT_PASSWORD}
    
    Press CTRL+C to stop the server
    """)
    
    log_action('SERVER_START', f'Server started on {host}:{port}')
    app.run(host=host, port=port, debug=debug)
