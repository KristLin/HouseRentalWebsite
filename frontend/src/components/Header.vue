<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <router-link class="navbar-brand" to="/">Airbnb</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/" active-class="active" exact>Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/contact" active-class="active" exact>Contact us</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/about" active-class="active" exact>About us</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/uploadHouse" active-class="active" exact>Upload</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/login" active-class="active" exact>Log in</router-link>
          </li>
          <li class="nav-item">
            <p class="nav-link mb-0" active-class="active" @click="logout">Log out</p>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
  methods: {
    logout() {
      window.console.log(
        "getters.isLoggedIn: ",
        this.$store.getters.isLoggedIn
      );
      if (this.$store.getters.isLoggedIn) {
        this.$axios
          .get("/api/users/logout/" + this.$store.getters.getUserId)
          .then(res => {
            if (res.status == 200) {
              this.$store.commit("logout");
              window.console.log("user logged out");
              alert("logged out!");
            }
          })
          .catch(err => window.console.log(err));
      } else {
        window.console.log("You are not logged in!");
        alert("You are not logged in!");
      }
    }
  }
};
</script>

<style scoped>
.navbar-brand {
  font-size: 2rem;
}
.navbar {
  min-height: 100px;
}
.nav-item::after {
  content: "";
  display: block;
  width: 0px;
  height: 2px;
  background: #3c9d9b;
  transition: 0.2s;
}
.nav-item:hover::after {
  width: 100%;
}
.navbar-dark .navbar-nav .active > .nav-link,
.navbar-dark .navbar-nav .nav-link.active,
.navbar-dark .navbar-nav .nav-link.show,
.navbar-dark .navbar-nav .show > .nav-link,
.navbar-dark .navbar-nav .nav-link:focus,
.navbar-dark .navbar-nav .nav-link:hover {
  color: #3c9d9b;
}
.nav-link {
  padding: 15px 5px;
  transition: 0.2s;
}
.dropdown-item.active,
.dropdown-item:active {
  color: #212529;
}
.dropdown-item:focus,
.dropdown-item:hover {
  background: #3c9d9b;
}
</style> 