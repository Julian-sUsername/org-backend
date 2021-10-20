<!-- HTML -->
<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Acogelo Mision TIC</h1>
      <nav>
        <button v-if="is_auth" v-on:click="loadHome">Inicio</button>
        <button v-if="is_auth" @click="loadAccount">Cuenta</button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <div class="footer">
      <h2>Acogelo 2022</h2>
    </div>
  </div>
</template>




<!-- Metodos -->
<script>
export default {
  name: "App",

  data: function () {
    //Por defecto en false, con esto se controla el login
    return {
      is_auth: false,
    };
  },

  components: {},

  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      //Si no esta autenticado se va Login
      if (this.is_auth == false) {
        this.$router.push({ name: "logIn" });
      } else {
        this.$router.push({ name: "home" });
      }
    },
    //Cambio de url
    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
    //Cambio de url
    loadSignUp: function () {
      this.$router.push({ name: "signUp" });
    },
    //Funciones Componentes hijos
    completedLogIn: function (data) {
      //Almacenamiento en el localStrorage
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      //Alerta
      alert("Autenticación Exitosa");
      //Verificar
      this.verifyAuth();
    },

    completedSignUp: function (data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },
    //Boton inicio
    loadHome: function () {
      this.$router.push({ name: "home" });
    },
    //Boton cerrar sesión
    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },
    //Ver cuenta
    loadAccount: function () {
      this.$router.push({ name: "account" });
    },
  },
  //Verificacion si el usuario esta logueado o no
  created: function () {
    this.verifyAuth();
  },
};
</script>




<!-- CSS -->
<style>
body {
  margin: 0 0 0 0;
}

.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;

  background-color: #283747;
  color: #e5e7e9;

  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  width: 20%;
  text-align: center;
}

.header nav {
  height: 100%;
  width: 20%;

  display: flex;
  justify-content: space-around;
  align-items: center;

  font-size: 20px;
}

.header nav button {
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 20px;
}

.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}

.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;

  background: #fdfefe;
}

.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;

  background-color: #283747;
  color: #e5e7e9;
}

.footer h2 {
  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}
</style>