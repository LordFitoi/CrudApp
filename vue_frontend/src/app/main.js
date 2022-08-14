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
        updateContact(entity) {
            this.store.isEditing = true;
            this.$refs.createModal.setFieldsValues({
                id: entity.id,
                role: entity.role,
                phone_number: entity.phone_number,
                postal_code: entity.postal_code,
                document_type: entity.document_type,
                entity_type: entity.entity_type,
                number: entity.number
            });
            this.toggleModalVisibility();
        },
        createContact() {
            this.store.isEditing = false;
            this.$refs.createModal.setFieldsValues({
                role: "User",
                phone_number: "",
                postal_code: "",
                document_type: "RNC",
                entity_type: "Juridical",
                number: ""
            });
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

