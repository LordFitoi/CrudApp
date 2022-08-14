<template>
    <div class="modal-container" :class="{ 'active': store.isModalVisible }" @click="toggleModalVisibility()">
        <div class="container mx-auto w-full grid grid-col-12 click-to-hide">
            <div class="modal-inner box col-span-sub-4 border border-primary" @click.stop>
                <h3 class="font-lg">Agendar Contacto</h3>
                <hr class="mb-4 w-full border border-secondary">
                <div class="form flex flex-col">
                    <div class="flex flex-col gap-4">
                        <div class="flex flex-col gap-2">
                            <p>Codigo Postal:</p>
                            <input type="text" name="last_name" placeholder="Codigo postal" v-model="postal_code">
                        </div>
                        <div class="flex flex-col gap-2">
                            <p>Numero de Documento:</p>
                            <input type="text" name="number" placeholder="302-212349-2" v-model="number">
                            <p v-if="numDocumentError && check" class="text-red font-sm">
                                Este campo es requerido.
                            </p>
                        </div>
                        <div class="flex flex-col gap-2">
                            <p>Telefono:</p>
                            <input type="tel" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" name="phone_number" placeholder="829-451-0140" v-model="phone_number">
                        </div>
                        <div class="flex flex-col gap-2">
                            <p>Role:</p>
                            <select name="role" v-model="role">
                                <option value="User">Usuario</option>
                                <option value="Admin">Admin</option>
                                <option value="Moderator">Moderador</option>
                            </select>
                        </div>
                         <div class="flex flex-col gap-2">
                            <p>Tipo de Documento:</p>
                            <select name="document_type" v-model="document_type">
                                <option value="RNC">RNC</option>
                                <option value="ID Card">Cedula</option>
                                <option value="Passport">Pasaporte</option>
                            </select>
                        </div>
                         <div class="flex flex-col gap-2">
                            <p>Tipo de Entidad:</p>
                            <select name="entity_type" v-model="entity_type">
                                <option value="Physical">Fisica</option>
                                <option value="Juridical">Juridica</option>
                            </select>
                        </div>
                        
                    </div>
                    
                    <div class="mt-10 flex gap-2 justify-end">
                        <button @click="toggleModalVisibility()" class="border flex justify-center px-6 py-2 rounded-1 click-to-hide">
                            Cancelar
                        </button>
                        <button @click="performSubmit()" class="border flex justify-center px-6 py-2 rounded-1">
                            <p v-if="store.isEditing">Actualizar</p>
                            <p v-else>Crear</p>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Store from '../app/store.js';

export default {
    setup() {
        return { store: Store() }
    },
    data() {
        return {
            id: null,
            check: false,
            role: "User",
            phone_number: "",
            postal_code: "",
            document_type: "RNC",
            entity_type: "Juridical",
            number: ""
        }
    },
    computed: {
        numDocumentError() {
            return this.number == "";
        },
    },
    methods: {
        getData() {
            return {
                role: this.role,
                phone_number: this.phone_number,
                postal_code: this.postal_code,
                document_type: this.document_type,
                entity_type: this.entity_type,
                number: this.number
            }
        },
        updateContact () {
            let data = this.getData();
            this.store.update(this.id, data).then(() => {
                this.toggleModalVisibility();
            });
        },
        setFieldsValues(data) {;
            this.id = data.id;
            this.role = data.role;
            this.phone_number = data.phone_number;
            this.postal_code = data.postal_code;
            this.document_type = data.document_type;
            this.entity_type = data.entity_type;
            this.number = data.number;
        },
        createContact() {
            let data = this.getData();
            this.store.create(data).then(() => {
                this.toggleModalVisibility();
            });
        },
        toggleModalVisibility() {
            this.store.isModalVisible = !this.store.isModalVisible;
            this.check = false;
        },
        performSubmit() {
            if (!this.numDocumentError) {
                if (this.store.isEditing) {
                    this.updateContact();
                } else {
                    this.createContact();
                }
            }

            this.check = true;
        }
    }
}
</script>
