<template>
  <div>
    <div class="container">
      <h3 class="mb-4">My Account</h3>
      <hr />
      <div class="row">
        <div class="col-lg-5 col-md-6 col-sm-4">
          <!-- user profile -->
          <img :src="userData.profile" class="user-profile" />
          
          <!-- select profile button -->
          <div class="profile-buttons-div mt-2">
            <input
              type="file"
              style="display: none"
              ref="fileInput"
              accept=".png, .jpg, .jpeg"
              @change="selectFile"
            />
            <button
              class="btn btn-outline-dark btn-sm form-control my-4"
              @click="$refs.fileInput.click()"
            >Select Profile</button>
            <!-- <button class="my-btn btn-sm form-control" @click="uploadProfile">Upload Profile</button> -->
          </div>
        </div>

        <!-- used as layout component -->
        <hr class="small-screen-layout" display="none" />

        <!-- user info labels -->
        <div class="col-lg-2 col-md-2 col-sm-2 text-right input-label-div">
          <label class="form-group form-control border-0">Email:</label>
          <label class="form-group form-control border-0">Name:</label>
          <label class="form-group form-control border-0">Phone:</label>
          <label class="form-group form-control border-0">Password:</label>
          <label class="form-group form-control border-0">Confirm:</label>
          <label class="form-group form-control border-0">Role:</label>
        </div>

        <!-- user info -->
        <div class="col-lg-5 col-md-4 col-sm-6">
          <div class="form-group">
            <input
              type="email"
              v-model="updatedUserData.email"
              class="form-control"
              :placeholder="userData.email"
              required
            />
          </div>
          <div class="form-group">
            <input
              v-model="updatedUserData.name"
              class="form-control"
              :placeholder="userData.name"
              required
            />
          </div>
          <div class="form-group">
            <input
              type="tel"
              v-model="updatedUserData.phone"
              class="form-control"
              :placeholder="userData.phone"
              required
            />
          </div>

          <div class="form-group">
            <input
              type="password"
              v-model="updatedUserData.password"
              class="form-control"
              placeholder="New Password"
              required
            />
          </div>
          <div class="form-group">
            <input
              type="password"
              v-model="updatedUserData.password2"
              class="form-control"
              placeholder="New Password Confirm"
              required
            />
          </div>
          <!-- choose role -->
          <div class="form-group mt-3">
            <div class="d-inline mx-1">
              <input
                type="radio"
                name="role"
                value="tenant"
                v-model="updatedUserData.role"
                class="mx-1"
              />
              <label>Tenant</label>
            </div>
            <div class="d-inline mx-1">
              <input
                type="radio"
                name="role"
                value="provider"
                v-model="updatedUserData.role"
                class="mx-1"
              />
              <label>Provider</label>
            </div>
          </div>
        </div>
      </div>
      <hr />
      <div class="button-area">
        <button class="my-btn form-control" @click="updateAccount">Update Account</button>
        <button class="btn btn-danger form-control my-1" @click="deleteAccount">Delete Account</button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
const defaultProfile = require("@/assets/user-default-profile.png");

export default {
  name: "myAccount",
  components: {},

  data() {
    return {
      userData: {},
      updatedUserData: {}
    };
  },

  methods: {
    selectFile(event) {
      window.console.log(event.target.files[0]);
      this.updatedUserData.profile = event.target.files[0];
      this.userData.profile = URL.createObjectURL(this.updatedUserData.profile);
      this.$forceUpdate();
    },
    async imageToUrl(imageFile) {
      // send image to imgbb API to get iamge's url
      let KEY = "587e7ebff1f6ee9c2fc6501859d37864";
      let HOST = "https://api.imgbb.com/1/upload?key=" + KEY;
      let formData = new FormData();
      formData.append("image", imageFile);
      return await this.$axios.post(HOST, formData);
    },
    async updateAccount() {
      // if one of the password input are not empty, check if they are matched
      if (this.updatedUserData.password || this.updatedUserData.password2) {
        if (this.updatedUserData.password !== this.updatedUserData.password2) {
          this.$swal("Warning", "Passwords are not matched!", "warning");
          return;
        }
      }

      let validUpdatedData = {};
      let validData = 0;

      if ("profile" in this.updatedUserData) {
        let profile = this.updatedUserData.profile;
        window.console.log("profile: ", profile);
        validData += 1;
        let res = await this.imageToUrl(profile);
        validUpdatedData.profile = res.data.data.url;
      }

      window.console.log(validUpdatedData);
      for (let key in this.updatedUserData) {
        if (key !== "profile" && key !== "password2") {
          if (this.updatedUserData[key] !== this.userData[key]) {
            validData += 1;
            validUpdatedData[key] = this.updatedUserData[key];
          }
        }
      }

      // if there is no valid data to update, show a warning dialog
      if (validData === 0) {
        this.$swal("Warning", "Nothing to update!", "warning");
        return;
      }

      // send update reuqest to backend
      this.$axios
        .patch("/api/users/" + this.$store.getters.getUserId, validUpdatedData)
        .then(response => {
          window.console.log(response);
          this.$swal("Success", "Your user data is updated!", "success");
          this.$forceUpdate();
        })
        .catch(error => window.console.log(error.response));
    },

    deleteAccount() {
      // need user to confirm the delete operation
      this.$swal({
        title: "Confirm",
        text: "Are you sure you want to delete your account?",
        icon: "warning",
        buttons: true,
        dangerMode: true
      }).then(choice => {
        if (choice) {
          // send delete request to backend
          this.$axios
            .delete("/api/users/" + this.$store.getters.getUserId)
            .then(response => {
              window.console.log(response);
              this.$swal("Success", "Your account is deleted!", "success");
              this.$store.commit("logout");
              this.$router.push({ name: "home" });
              window.location.reload(true);
            })
            .catch(error => window.console.log(error.response));
        }
      });
    }
  },
  created() {
    if (!this.$store.getters.isLoggedIn) {
      window.console.log("Require log in!");
      this.$router.push({ name: "home" });
    }
    this.$axios
      .get("/api/users/" + this.$store.getters.getUserId)
      .then(response => {
        this.userData = response.data;
        this.updatedUserData.role = this.userData.role;

        if (!("profile" in this.userData)) {
          this.userData.profile = defaultProfile;
        }
      })
      .catch(error => {
        window.console.log(error);
      });
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
  margin-top: 100px;
  margin-bottom: 80px;
}

.user-profile {
  width: 250px;
  height: 250px;
  object-fit: cover;
  border-radius: 50%;
}

.profile-buttons-div {
  margin: auto;
  width: 150px;
}

.button-area {
  margin: auto;
  width: 300px;
}

.my-btn {
  border: none;
  background-color: black;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: #3c9d9b;
  color: white;
}

@media screen and (max-width: 768px) {
  .user-profile {
    margin-top: 3.5rem;
    width: 150px;
    height: 150px;
    object-fit: cover;
  }
}

@media screen and (max-width: 576px) {
  .input-label-div {
    display: none;
  }
  .user-profile-div {
    margin-bottom: 2rem;
  }
}
</style>