<template>
    <!-- Password Reset Page -->
    <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/plus/img/logos/mark.svg?color=teal&shade=600" alt="Your Company">
        <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">Reset your password</h2>
      </div>
    
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" action="#" method="POST">
          <div>
            <label for="email" class="block text-sm/6 font-medium text-gray-900">Enter the email address associated with your account and we will send you a password reset link</label>
            <div class="mt-2">
              <input id="email" name="email" type="email" autocomplete="email" placeholder="Email Address" required class="block w-full rounded-md border-0 py-1.5 px-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-teal-600 sm:text-sm/6">
            </div>
          </div>
    
          <div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-teal-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-teal-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-600">
              Send Password Reset Link
            </button>
          </div>
        </form>
    
      </div>
    </div>
    </template>
    
    <script>
    definePageMeta({
        layout: 'auth',
    })
    </script>