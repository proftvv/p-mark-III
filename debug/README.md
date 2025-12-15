# Debug Configuration

**Project**: P-Mark-III  
**Version**: 1.0.1

---

## Debug Settings

```json
{
  "debug_mode": true,
  "log_level": "INFO",
  "log_file": "debug/debug.log",
  "console_output": true,
  "log_api_calls": true,
  "log_database_queries": true,
  "log_user_actions": true,
  "performance_monitoring": true,
  "error_stack_traces": true
}
```

---

## Log Levels

- **DEBUG**: Detailed information for debugging
- **INFO**: General information about system operation
- **WARNING**: Warning messages for potential issues
- **ERROR**: Error messages for failures
- **CRITICAL**: Critical issues requiring immediate attention

---

## Testing Guidelines

1. **Unit Tests**: Test individual functions/modules
2. **Integration Tests**: Test component interactions
3. **API Tests**: Test Google Maps API integration
4. **UI Tests**: Test web interface functionality
5. **End-to-End Tests**: Test complete user workflows

---

## Test Checklist

### Authentication Tests
- [ ] Login with correct credentials
- [ ] Login with incorrect credentials
- [ ] Session management
- [ ] Logout functionality

### Search Tests
- [ ] Valid location search
- [ ] Invalid location handling
- [ ] Radius parameter validation
- [ ] Keyword filtering
- [ ] Empty results handling

### Data Collection Tests
- [ ] API response parsing
- [ ] Data field extraction
- [ ] Error handling for missing data
- [ ] Multiple results processing

### Excel Export Tests
- [ ] File generation
- [ ] Data formatting
- [ ] File download
- [ ] Filename generation

### System Tests
- [ ] Application startup
- [ ] CMD command execution
- [ ] Port availability
- [ ] Resource cleanup

---

## Debug Commands

### Start in Debug Mode
```bash
# To be implemented
python app.py --debug
```

### Run Tests
```bash
# To be implemented
python -m pytest tests/
```

### View Logs
```bash
# To be implemented
tail -f debug/debug.log
```

---

## Mock Data for Testing

*To be added when data structure is finalized*

---
