import axios from 'axios';
import settings from './settings.js';

export default axios.create({
    baseURL: settings.API_ROOT_URL,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': settings.CSRF_TOKEN
    }
})
