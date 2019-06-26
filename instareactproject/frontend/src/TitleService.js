import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class TitleService{

    constructor(){}

    getTitle(titleName) {
        const url = `${API_URL}/api/title?titleName=${titleName}`;
        return axios.get(url).then(response => response.data);
    }

    getTitles(titleName) {
        const url = `${API_URL}/api/title?query=${titleName}`;
        return axios.get(url).then(response => response.data);
    }

    getTitleCast(titleId) {
        const url = `${API_URL}/api/title/${titleId}/cast`;
        return axios.get(url).then(response => response.data);
    }
}