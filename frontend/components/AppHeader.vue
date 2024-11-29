<template>
    <!-- Navbar -->
    <nav class="w-full px-8 text-gray-700 bg-white">
        <div class="container flex flex-col flex-wrap items-center justify-between py-5 mx-auto md:flex-row max-w-7xl">
            <div class="relative flex flex-col md:flex-row">
                <NuxtLink to="/" class="flex items-center mb-5 font-medium text-gray-900 lg:w-auto lg:items-center lg:justify-center md:mb-0">
                    <span class="mx-auto text-xl font-black leading-none text-gray-900 select-none">Project Manager<span class="text-teal-600">.</span></span>
                </NuxtLink>
            </div>

            <div class="inline-flex items-center ml-5 space-x-6 lg:justify-end">
                <NuxtLink to="/login" class="btn btn-md btn-primary">
                    Sign in
                </NuxtLink>
                <NuxtLink to="/signup" class="btn btn-md btn-outline">
                    Sign up
                </NuxtLink>
            </div>
        </div>
    </nav>
</template>
