import { createApp } from 'vue'
import { createPinia } from 'pinia'

import Store from './store.js';
import CreateContactModal from '../components/create-contact-modal.vue';

createApp({
    components: { CreateContactModal },
    setup() {
        return { store: Store() }
    },
    mounted() {
        this.store.fetch();
    },
    methods: {
        updateContact(contact) {
            this.store.isEditing = true;
            this.$refs.createModal.setFieldsValues({
                id: contact.id,
                first_name: contact.first_name,
                last_name: contact.last_name,
                email: contact.email,
                phone_number: contact.phone_number,
                relation_ship: contact.relation_ship
            });
            this.toggleModalVisibility();
        },
        createContact() {
            this.store.isEditing = false;
            this.toggleModalVisibility();
        },
        toggleModalVisibility() {
            this.store.isModalVisible = !this.store.isModalVisible;
        },
        deleteContact(id) {
            this.store.delete(id);
        }
    }
})
.use(createPinia())
.mount('#app')

