// P-Mark-III - Main JavaScript
// Version: 1.0.2

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 P-Mark-III v1.0.2 - Loaded');
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s ease';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
    
    // Add loading animation to login button
    const loginForm = document.querySelector('.login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            submitBtn.textContent = 'Giriş yapılıyor...';
            submitBtn.disabled = true;
        });
    }
    
    // Console welcome message
    console.log('%c P-Mark-III ', 'background: #3498db; color: white; font-size: 20px; padding: 10px;');
    console.log('%c Business Intelligence System v1.0.2 ', 'background: #2ecc71; color: white; font-size: 14px; padding: 5px;');
});
