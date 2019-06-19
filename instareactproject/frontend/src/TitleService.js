import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class TitleService{

    constructor(){}

    getTitle(titleName) {
        const url = `${API_URL}/api/title/${titleName}`;
        return axios.get(url).then(response => response.data);
    }
}