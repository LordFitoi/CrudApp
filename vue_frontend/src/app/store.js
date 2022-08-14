import  { defineStore } from 'pinia';
import client from '../utils/http-client.js';

export default defineStore('contact-store', {
    state: () => {
        return {
            contacts: [],
            isModalVisible: false,
            isEditing: false,
        }
    },
    actions: {
        create(data) {
            return client.post('/contacts/', data).then((response) => {
                this.contacts.push(response.data);
            });
        },
        fetch() {
            return client.get(`/contacts/`).then((response) => {
                this.contacts = response.data;
            })
        },
        update(id, data) {
            return client.put(`/contacts/${id}/`, data).then((response) => {
                this.contacts.forEach((contact, index) => {
                    if (contact.id === response.data.id) {
                        this.contacts[index] = response.data;
                    }
                });
            })
        },
        delete(id) {
            return client.delete(`/contacts/${id}`).then(() => {
                this.contacts = this.contacts.filter((contact) => contact.id !== id);
            })
        }
    }
})