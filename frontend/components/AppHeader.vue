<template>
    <!-- Navbar -->
    <nav class="w-full px-8 text-gray-700 bg-white">
        <div class="container flex flex-col flex-wrap items-center justify-between py-5 mx-auto md:flex-row max-w-7xl">
            <div class="relative flex flex-col md:flex-row">
                <NuxtLink to="#_" class="flex items-center mb-5 font-medium text-gray-900 lg:w-auto lg:items-center lg:justify-center md:mb-0">
                    <span class="mx-auto text-xl font-black leading-none text-gray-900 select-none">Project Manager<span class="text-teal-600">.</span></span>
                </NuxtLink>
            </div>

            <div class="inline-flex items-center ml-5 space-x-6 lg:justify-end">
                <NuxtLink to="/login" class="text-base font-medium leading-6 text-gray-600 whitespace-no-wrap transition duration-150 ease-in-out hover:text-gray-900">
                    Sign in
                </NuxtLink>
                <NuxtLink to="/signup" class="inline-flex items-center justify-center px-4 py-2 text-base font-medium leading-6 text-white whitespace-no-wrap bg-teal-600 border border-transparent rounded-md shadow-sm hover:bg-teal-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-600">
                    Sign up
                </NuxtLink>
            </div>
        </div>
    </nav>
</template>
