<template>

    <div class="signUp_user">
        <div class="container_signUp_user">
            <h2>Registrarse</h2>

            <form v-on:submit.prevent="processSignUp" >
                <input type="text" v-model="user.username" placeholder="Username">
                <br>
                
                <input type="password" v-model="user.password" placeholder="Password">
                <br>
                
                <input type="text" v-model="user.nombres" placeholder="Nombres">
                <br>

                 <input type="text" v-model="user.apellidos" placeholder="Apellidos">
                <br>

                <input type="email" v-model="user.email" placeholder="Email">
                <br>

                 <input type="text" v-model="user.rol" placeholder="Rol">
                <br>

                <input type="number" v-model="user.celular" placeholder="Celular">
                <br>

                <input type="text" v-model="user.horario_contacto" placeholder="Horario de contacto">
                <br>

                <input type="text" v-model="user.dpto_residencia" placeholder="Departamento de residencia">
                <br>

                 <input type="text" v-model="user.ciudad_residencia" placeholder="Ciudad de residencia">
                <br>
                
                <input type="checkbox" v-model="user.aceptacion_termycond" placeholder="Acepta terminos y condiciones"> Acepto terminos y condiciones
                <br>

                <button type="submit">Registrarse</button>
            </form>
        </div>

    </div>

</template>




<script>
import axios from 'axios';

export default {
    name: "SignUp",

    data: function(){
        return {
            user: {
                username: "",
                password: "",
                nombres: "",
                apellidos: "",
                email: "",
                rol: "",
                celular: null,
                horario_contacto: "",
                dpto_residencia: "",
                ciudad_residencia: "",
                aceptacion_termycond: null
            }
        }
    },

    methods: {
        processSignUp: function(){
            axios.post(
                "https://server-acogelo.herokuapp.com/user/", 
                this.user,  
                {headers: {}}
            )
                .then((result) => {
                    let dataSignUp = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    
                    this.$emit('completedSignUp', dataSignUp)
                })
                .catch((error) => {
                    console.log(error)
                    alert("Erroe en el resgistro.");
                    
                    
                });
        }
    }
}
</script>



<style>

    .signUp_user{
        margin: 0;
        padding: 0%;
        height: 500px;
        width: 100%;
    
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_signUp_user {
        border: 3px solid  #283747;
        border-radius: 10px;
        width: 35%;
        height: 90%;

        
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .signUp_user h2{
        color: #283747;

    }

    .signUp_user form{
        width: 80%;
        
    }

    .signUp_user input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;

        border: 1px solid #283747;
    }

    .signUp_user button{
        width: 100%;
        height: 40px;

        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }

    .signUp_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }

</style>