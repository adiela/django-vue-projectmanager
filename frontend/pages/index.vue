<template>
    
<!-- Section 1 -->
<section class="w-full px-8 text-gray-700 bg-white">
    <nav class="container flex flex-col flex-wrap items-center justify-between py-5 mx-auto md:flex-row max-w-7xl">
        <div class="relative flex flex-col md:flex-row">
            <a href="#_" class="flex items-center mb-5 font-medium text-gray-900 lg:w-auto lg:items-center lg:justify-center md:mb-0">
                <span class="mx-auto text-xl font-black leading-none text-gray-900 select-none">Project Manager<span class="text-teal-600">.</span></span>
            </a>
        </div>

        <div class="inline-flex items-center ml-5 space-x-6 lg:justify-end">
            <a href="#" class="text-base font-medium leading-6 text-gray-600 whitespace-no-wrap transition duration-150 ease-in-out hover:text-gray-900">
                Sign in
            </a>
            <a href="#" class="inline-flex items-center justify-center px-4 py-2 text-base font-medium leading-6 text-white whitespace-no-wrap bg-teal-600 border border-transparent rounded-md shadow-sm hover:bg-teal-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-600">
                Sign up
            </a>
        </div>
    </nav>
</section>

<!-- Section 2 -->
<section class="px-2 py-32 bg-white md:px-0">
  <div class="container items-center max-w-6xl px-8 mx-auto xl:px-5">
    <div class="flex flex-wrap items-center sm:-mx-3">
      <div class="w-full md:w-1/2 md:px-3">
        <div class="w-full pb-6 space-y-6 sm:max-w-md lg:max-w-lg md:space-y-4 lg:space-y-8 xl:space-y-9 sm:pr-5 lg:pr-0 md:pb-0">
          <h1 class="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl md:text-4xl lg:text-5xl xl:text-6xl">
            <span class="block xl:inline">Manage your Projects </span>
            <span class="block text-teal-600 xl:inline">Seamlessly</span>
          </h1>
          <p class="mx-auto text-base text-gray-500 sm:max-w-md lg:text-xl md:max-w-3xl">It's never been easier to manage your projects.</p>
          <div class="relative flex flex-col sm:flex-row sm:space-x-4">
            <a href="#_" class="flex items-center w-full px-6 py-3 mb-3 text-lg text-white bg-teal-600 rounded-md sm:mb-0 hover:bg-teal-700 sm:w-auto">
              View Demo Project Board
              <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 ml-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </div>
      </div>
      <div class="w-full md:w-1/2">
        <div class="w-full h-auto overflow-hidden rounded-md shadow-xl sm:rounded-xl">
            <img src="~/assets/images/screens.png">
          </div>
      </div>
    </div>
  </div>
</section>

<!-- Section 3 -->
<section class="w-full bg-white pt-7 pb-7 md:pt-20 md:pb-24">
    <div class="box-border flex flex-col items-center content-center px-8 mx-auto leading-6 text-black border-0 border-gray-300 border-solid md:flex-row max-w-7xl lg:px-16">

        <!-- Image -->
        <div class="box-border relative w-full max-w-md px-4 mt-5 mb-4 -ml-5 text-center bg-no-repeat bg-contain border-solid md:ml-0 md:mt-0 md:max-w-none lg:mb-0 md:w-1/2 xl:pl-10">
            <img src="~/assets/images/checklist.png" class="p-2 pl-6 pr-5 xl:pl-16 xl:pr-20 ">
        </div>

        <!-- Content -->
        <div class="box-border order-first w-full text-black border-solid md:w-1/2 md:pl-10 md:order-none">
            <h2 class="m-0 text-xl font-semibold leading-tight border-0 border-gray-300 lg:text-3xl md:text-2xl">
                Create Projects on the fly
            </h2>
            <p class="pt-4 pb-8 m-0 leading-7 text-gray-700 border-0 border-gray-300 sm:pr-12 xl:pr-32 lg:text-lg">
                Project Manager allows you to create projects on the fly. Get started now and start managing your projects seamlessly.
            </p>
            <ul class="p-0 m-0 leading-6 border-0 border-gray-300">
                <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                    <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-teal-300 rounded-full"><span class="text-sm font-bold">✓</span></span> Create multiple projects
                </li>
                <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                    <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-teal-300 rounded-full"><span class="text-sm font-bold">✓</span></span> Add team members to your projects
                </li>
                <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                    <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-teal-300 rounded-full"><span class="text-sm font-bold">✓</span></span> Create tasks and assign them to team members
                </li>
            </ul>
        </div>
        <!-- End  Content -->
    </div>
    <div class="box-border flex flex-col items-center content-center px-8 mx-auto mt-2 leading-6 text-black border-0 border-gray-300 border-solid md:mt-20 xl:mt-0 md:flex-row max-w-7xl lg:px-16">

        <!-- Content -->
        <div class="box-border w-full text-black border-solid md:w-1/2 md:pl-6 xl:pl-32">
            <h2 class="m-0 text-xl font-semibold leading-tight border-0 border-gray-300 lg:text-3xl md:text-2xl">
                Track your progress of your projects
            </h2>
            <p class="pt-4 pb-8 m-0 leading-7 text-gray-700 border-0 border-gray-300 sm:pr-10 lg:text-lg">
                Project Manager allows you to track the progress of your projects. Get detailed insights on your projects.
            </p>
            <ul class="p-0 m-0 leading-6 border-0 border-gray-300">
                <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                    <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-teal-300 rounded-full"><span class="text-sm font-bold">✓</span></span> Update the status of your projects
                </li>
                <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                    <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-teal-300 rounded-full"><span class="text-sm font-bold">✓</span></span> Update the progress of tasks
                </li>
                <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                    <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-teal-300 rounded-full"><span class="text-sm font-bold">✓</span></span> Add comments to tasks
                </li>
            </ul>
        </div>
        <!-- End  Content -->

        <!-- Image -->
        <div class="box-border relative w-full max-w-md px-4 mt-10 mb-4 text-center bg-no-repeat bg-contain border-solid md:mt-0 md:max-w-none lg:mb-0 md:w-1/2">
            <img src="~/assets/images/clipboard.jpg" class="pl-4 sm:pr-10 xl:pl-10 lg:pr-32">
        </div>
    </div>
</section>

<!-- Section 4 -->
<section class="py-20 bg-gray-50">
  <div class="container items-center max-w-6xl px-4 px-10 mx-auto sm:px-20 md:px-32 lg:px-16">
    <div class="flex flex-wrap items-center -mx-3">
      <div class="order-1 w-full px-3 lg:w-1/2 lg:order-0">
        <div class="w-full lg:max-w-md">
          <h2 class="mb-4 text-3xl font-bold leading-tight tracking-tight sm:text-4xl font-heading">Jam-packed with all the tools you need to succeed!</h2>
          <p class="mb-4 font-medium tracking-tight text-gray-400 xl:mb-6">It's never been easier to manage your projects. Our tools will help you with the following:</p>
          <ul>
            <li class="flex items-center py-2 space-x-4 xl:py-3">
              <svg class="w-8 h-8 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path></svg>
              <span class="font-medium text-gray-500">Easy to use interface</span>
            </li>
            <li class="flex items-center py-2 space-x-4 xl:py-3">
              <svg class="w-8 h-8 text-teal-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
              <span class="font-medium text-gray-500">Track progress</span>
            </li>
            <li class="flex items-center py-2 space-x-4 xl:py-3">
              <svg class="w-8 h-8 text-pink-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
              <span class="font-medium text-gray-500">Add details</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="w-full px-3 mb-12 lg:w-1/2 order-0 lg:order-1 lg:mb-0"><img class="mx-auto sm:max-w-sm lg:max-w-full" src="~/assets/images/triple-icons.png" alt="feature image"></div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="bg-white">
    <div class="max-w-screen-xl px-4 py-12 mx-auto space-y-8 overflow-hidden sm:px-6 lg:px-8">
        <p class="mt-8 text-base leading-6 text-center text-gray-400">
            © {{ new Date().getFullYear() }} Built by <a href="https://gtihub.com/adiela" class="text-teal-600">Adiela Abishua</a>. Licensed under the MIT License.
        </p>
    </div>
</footer>
</template>