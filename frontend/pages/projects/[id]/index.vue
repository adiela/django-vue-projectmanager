<template>
<div class="flex flex-col w-screen h-screen overflow-auto text-gray-700 bg-gradient-to-tr from-blue-200 via-indigo-200 to-pink-200">
	<div class="px-10 mt-6">
		<h1 class="text-2xl font-bold">Team Project Board</h1>
	</div>
	<div class="flex flex-grow px-10 mt-4 space-x-6 overflow-auto">
		<TaskList v-for="list in Array(3)" />
	</div>
</div>
</template>