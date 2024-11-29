<template>
<!-- Login Page -->
<div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
  <div class="sm:mx-auto sm:w-full sm:max-w-sm">
    <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/plus/img/logos/mark.svg?color=teal&shade=600" alt="Your Company">
    <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">Sign in to your account</h2>
  </div>

  <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
    <form class="space-y-6" action="#" method="POST">
      <fieldset class="input-group">
        <label for="email" class="block text-sm/6 font-medium text-gray-900">Email address</label>
        <input id="email" name="email" type="email" autocomplete="email" required class="w-full form-input">
      </fieldset>

      <div>
        <div class="flex items-center justify-between">
          <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>
          <div class="text-sm">
            <NuxtLink to="/password_reset" class="font-semibold text-teal-600 hover:text-teal-500">Forgot password?</NuxtLink>
          </div>
        </div>
          <input id="password" name="password" type="password" autocomplete="current-password" required class="form-input w-full">

      </div>

        <button type="submit" class="btn btn-md btn-primary w-full">Sign in</button>
    </form>
    <button type="submit" class="btn btn-md btn-outline w-full mt-5">Sign in with Github</button>

    <p class="mt-10 text-center text-sm/6 text-gray-500">
      Don't have an account?
      <NuxtLink to="/signup" class="font-semibold text-teal-600 hover:text-teal-500">Create an account</NuxtLink>
    </p>
  </div>
</div>
</template>

<script>
definePageMeta({
    layout: 'auth',
})

export default {
  head() {
    return {
      title: 'Login',
    }
  },
  methods: {
    async loginWithEmail() {
      try {
        const response = await fetch(`${process.env.VUE_APP_BACKEND_URL}/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          })
        })
        .then(response => response.json())
        .then(data => {
          this.$store.commit('setUser', data);
          this.$router.push('/dashboard');
        });
      } catch {
        console.error('Failed to login');

      }
    },
    async loginWithGithub() {
      try {
        const response = await fetch(`${process.env.VUE_APP_BACKEND_URL}/login/github`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(response => response.json())
        .then(data => {
          this.$store.commit('setUser', data);
          this.$router.push('/dashboard');
        });
      } catch {
        console.error('Failed to login with Github');
      }
    }
  }
}
</script>