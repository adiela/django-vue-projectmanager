<template>
<!-- Signup Page -->
<div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
  <div class="sm:mx-auto sm:w-full sm:max-w-sm">
    <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/plus/img/logos/mark.svg?color=teal&shade=600" alt="Your Company">
    <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">Create an account</h2>
  </div>

  <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
    <form class="space-y-6" action="#" method="POST">
      <fieldset class="input-group">
        <label for="email" class="form-label">Email address</label>
        <input id="email" name="email" type="email" autocomplete="email" required class="w-full form-input">
      </fieldset>

      <fieldset class="input-group">
        <label for="password" class="form-label">Password</label>
        <input id="password1" name="password1" type="password" autocomplete="current-password" required class="form-input w-full">
      </fieldset>

      <fieldset class="input-group">
        <label for="password" class="form-label">Confirm Password</label>
        <input id="password2" name="password2" type="password" autocomplete="current-password" required class="form-input w-full">
      </fieldset>

      <button type="submit" class="btn btn-md btn-primary w-full">Sign Up</button>
         
    </form>
    <button type="button" class="btn btn-md btn-outline mt-5 w-full">Sign in with Github</button>


    <p class="mt-10 text-center text-sm/6 text-gray-500">
      Already have an account?
      <NuxtLink to="/login" class="font-semibold text-teal-600 hover:text-teal-500">Sign into your account</NuxtLink>
    </p>
  </div>
</div>
</template>

<script>
definePageMeta({
    layout: 'auth',
})
</script>