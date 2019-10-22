<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-lg-5 col-md-6 col-sm-4">
          <img :src="userData.profile" class="user-profile" />
          <!-- <br /> -->
          <div class="profile-buttons-div mt-2">
            <input type="file" style="display: none" ref="fileInput" @change="selectFile" />
            <button
              class="my-btn btn-sm form-control my-2"
              @click="$refs.fileInput.click()"
            >Select Profile</button>
            <button class="my-btn btn-sm form-control" @click="uploadProfile">Upload Profile</button>
          </div>
        </div>
        <hr class="small-screen-layout" display="none" />
        <div class="col-lg-2 col-md-2 col-sm-2 text-right input-label-div">
          <label class="form-group form-control border-0">Email:</label>
          <label class="form-group form-control border-0">Name:</label>
          <label class="form-group form-control border-0">Phone:</label>
          <label class="form-group form-control border-0">Password:</label>
          <label class="form-group form-control border-0">Confirm:</label>
          <label class="form-group form-control border-0">Role:</label>
        </div>
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
      updatedUserData: {},
      userProfile: ""
    };
  },

  methods: {
    selectFile(event) {
      window.console.log(event.target.files[0]);
      this.updatedUserData.profile = event.target.files[0];
      this.userData.profile = URL.createObjectURL(this.updatedUserData.profile);
      this.$forceUpdate();
    },
    uploadProfile() {
      let formData = new FormData();
      formData.append(
        "profile",
        this.updatedUserData.profile,
        this.updatedUserData.profile.name
      );
      this.$axios
        .post("/api/users/profile/" + this.$store.getters.getUserId, formData, {
          onUploadProgress: function(progressEvent) {
            let percentCompleted = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            window.console.log("Upload Progress: ", percentCompleted + "%");
          }
        })
        .then(response => {
          this.userData.profile = URL.createObjectURL(
            this.updatedUserData.profile
          );
          this.$forceUpdate();
          window.console.log(response);
        })
        .catch(error => {
          window.console.log(error);
        });
    },

    updateAccount() {
      // if one of the password input are not empty, check if they are matched
      if (this.updatedUserData.password || this.updatedUserData.password2) {
        if (this.updatedUserData.password !== this.updatedUserData.password2) {
          alert("Passwords not matched!");
          return;
        }
      }

      let formData = new FormData();
      let validData = 0;

      if ("profile" in this.updatedUserData) {
        validData += 1;
        formData.append(
          "profile",
          this.updatedUserData.profile,
          this.updatedUserData.profile.name
        );
      }

      let usedUpdatedUserData = {};
      // remove invalid update data
      for (let key in this.updatedUserData) {
        if (this.updatedUserData[key] !== "" && key !=="password2" && key !== "profile") {
          if (this.updatedUserData[key] !== this.userData[key]) {
            usedUpdatedUserData[key] = this.updatedUserData[key]
            validData += 1;
          }
        }
      }

      if (validData === 0) {
        alert("Nothing to update!");
        return;
      }
      // window.console.log(usedUpdatedUserData)
      
      // transform Object to a File-like object
      let json = JSON.stringify(usedUpdatedUserData);
      let blob = new Blob([json], {
        type: "application/json"
      });

      // append transformed userData to form data
      formData.append("userData", blob);

      this.$axios
        .patch("/api/users/" + this.$store.getters.getUserId, formData, {
          onUploadProgress: function(progressEvent) {
            let percentCompleted = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            window.console.log("Upload Progress: ", percentCompleted + "%");
          }
        })
        .then(response => {
          if (response.status === 200) {
            if ("profile" in this.updatedUserData) {
              this.userData.profile = URL.createObjectURL(
                this.updatedUserData.profile
              );
              this.$forceUpdate();
            }

            window.console.log(response);
            alert("User info is updated!");
          }
        })
        .catch(error => {
          window.console.log(error);
        });

      // this.$axios
      //   .patch(
      //     "/api/users/" + this.$store.getters.getUserId,
      //     usedUpdatedUserData
      //   )
      //   .then(response => {
      //     window.console.log(response);
      //     alert("User info is updated!");
      //   })
      //   .catch(error => window.console.log(error.response));
    },

    deleteAccount() {
      this.$axios
        .delete("/api/users/" + this.$store.getters.getUserId)
        .then(response => {
          window.console.log(response);
          alert("User account is deleted!");
          this.$store.commit("logout");
          this.$router.push({ name: "home" });
        })
        .catch(error => window.console.log(error.response));
    }
  },
  created() {
    if (!this.$store.getters.isLoggedIn) {
      alert("Require login!");
      this.$router.push({ name: "home" });
    }
    this.$axios
      .get("/api/users/" + this.$store.getters.getUserId)
      .then(response => {
        this.userData = response.data;
        this.updatedUserData.role = this.userData.role;

        if ("profile" in this.userData) {
          this.userData.profile="data:image/png;base64," + this.userData.profile
          // window.console.log(this.userData.profile)
        } else {
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