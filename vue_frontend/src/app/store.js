import  { defineStore } from 'pinia';
import client from '../utils/http-client.js';

export default defineStore('contact-store', {
    state: () => {
        return {
            entities: [],
            isModalVisible: false,
            isEditing: false,
        }
    },
    actions: {
        create(data) {
            return client.post('/entity/', data).then((response) => {
                this.entities.push(response.data);
            });
        },
        fetch() {
            return client.get(`/entity/`).then((response) => {
                this.entities = response.data;
            })
        },
        update(id, data) {
            return client.put(`/entity/${id}/`, data).then((response) => {
                this.entities.forEach((contact, index) => {
                    if (contact.id === response.data.id) {
                        this.entities[index] = response.data;
                    }
                });
            })
        },
        delete(id) {
            return client.delete(`/entity/${id}`).then(() => {
                this.entities = this.entities.filter((contact) => contact.id !== id);
            })
        }
    }
})