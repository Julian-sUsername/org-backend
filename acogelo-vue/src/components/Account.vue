<template>

    <div v-if="loaded" class="information">
        <h1>Información de su cuenta</h1>
        <h2>Username: <span>{{username}}</span></h2>
        <h2>Nombres: <span>{{nombres}}</span></h2>
        <h2>Apellidos: <span>{{apellidos}}</span></h2>
        <h2>Correo electrónico: <span>{{email}}</span></h2>
        <!--<h2>Departamento: <span>{{dpto_residencia}}</span></h2>
        <h2>ciudad: <span>{{ciudad_residencia}}</span></h2>-->
    </div>

</template>


<script>
import jwt_decode from "jwt-decode";
import axios from 'axios';

export default {
    name: "Account",
    //Se guarda la info que se trae del db
    data: function(){
        return {
            username: "",
            nombres: "",
            apellidos: "",
            email: "",
            loaded: false,
        }
    },

    methods: {
        getData: async function () {

            if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
                this.$emit('logOut');
                return;
			}
            //Esperar a verificar
            await this.verifyToken();
            
            let token = localStorage.getItem("token_access");
            //Desencriptar el access token
            let userId = jwt_decode(token).user_id.toString();
            
            axios.get(`https://server-acogelo.herokuapp.com/user/${userId}/`, {headers: {'Authorization': `Bearer ${token}`}})
                .then((result) => {
                    //Inicializar los valores cuando se traen del get
                    this.username = result.data.username;
                    this.nombres = result.data.nombres;
                    this.apellidos = result.data.apellidos;
                    //this.celular = result.data.celular;
                    this.email = result.data.email;
                    //this.dpto_residencia = result.data.dpto_residencia;
                    //this.ciudad_residencia = result.data.ciudad_residencia;
                    //Rederizar la informacion
                    this.loaded = true;
                    })
                .catch(() => {
                    this.$emit('logOut');
                });
        },

        verifyToken: function () {
            //Verificar 
            return axios.post("https://server-acogelo.herokuapp.com/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}})
				.then((result) => {
                    //Cambio del storage
					localStorage.setItem("token_access", result.data.access);		
				})
                //Por si hay error, get out
				.catch(() => {
					this.$emit('logOut');
				});
        }
    },

    created: async function(){
        this.getData();
    },
}
</script>


<style>
    .information{
        margin: 0;
        padding: 0%;
        width: 100%;
        height: 100%;

        display: flex;
        flex-direction: column;
        justify-content: center;    
        align-items: center;
    }

    .information h1{
        font-size: 60px;
        color: #0f1316;
    }

    .information h2{
        font-size: 40px;
        color: #283747;
    }

    .information span{
        color: crimson;
        font-weight: bold;
    }
</style>