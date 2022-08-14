<template>
    <div class="modal-container" :class="{ 'active': store.isModalVisible }" @click="toggleModalVisibility()">
        <div class="container mx-auto w-full grid grid-col-12 click-to-hide">
            <div class="modal-inner box col-span-sub-4 border border-primary" @click.stop>
                <h3 class="font-lg">Agendar Contacto</h3>
                <hr class="mb-4 w-full border border-secondary">
                <div class="form flex flex-col">
                    <div class="flex flex-col gap-4">
                        <div class="flex flex-col gap-2">
                            <p>Nombres:</p>
                            <input type="text" name="first_name" placeholder="Juancito Manuel" v-model="first_name">
                            <p v-if="fistNameError && check" class="text-red font-sm">
                                Este campo es obligatorio
                            </p>
                        </div>
                        <div class="flex flex-col gap-2">
                            <p>Apellidos:</p>
                            <input type="text" name="last_name" placeholder="Perez Rodriguez" v-model="last_name">
                        </div>
                        <div class="flex flex-col gap-2">
                            <p>Correo:</p>
                            <input type="email" name="email" placeholder="juancito@gmail.com" v-model="email">
                            <p v-if="emailError && check" class="text-red font-sm">
                                El correo debe incluir una @ para ser valido.
                            </p>
                        </div>
                        <div class="flex flex-col gap-2">
                            <p>Telefono:</p>
                            <input type="tel" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" name="phone_number" placeholder="829-451-0140" v-model="phone_number">
                        </div>
                        <div class="flex flex-col gap-2">
                            <p>Relacion:</p>
                            <select name="relation_ship" v-model="relation_ship">
                                <option value="Friend">Amigo</option>
                                <option value="Family">Familia</option>
                                <option value="Work">Trabajo</option>
                                <option value="Other">Otro</option>
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
            first_name: "",
            last_name: "",
            email: "",
            phone_number: "",
            relation_ship: "Other",
            check: false
        }
    },
    computed: {
        fistNameError() {
            return this.first_name == "";
        },
        emailError() {
            return !this.email.includes("@");
        }
    },
    methods: {
        getData() {
            return {
                first_name: this.first_name,
                last_name: this.last_name,
                email: this.email,
                phone_number: this.phone_number,
                relation_ship: this.relation_ship
            }
        },
        updateContact () {
            let data = this.getData();
            this.store.update(this.id, data).then(() => {
                this.toggleModalVisibility();
            });
        },
        setFieldsValues(data) {
            this.id = data.id;
            this.first_name = data.first_name;
            this.last_name = data.last_name;
            this.email = data.email;
            this.phone_number = data.phone_number;
            this.relation_ship = data.relation_ship;
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
            if (!this.fistNameError && !this.emailError) {
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
