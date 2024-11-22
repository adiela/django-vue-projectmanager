<template>
<div class="flex flex-col w-screen text-gray-700 bg-gradient-to-tr from-blue-200 via-indigo-200 to-pink-200 py-10">
	<div class="px-10 mt-6">
		<h1 class="text-2xl font-bold text-center">Team Project Board</h1>
	</div>
	<div class="flex flex-grow px-10 mt-4 space-x-6 overflow-x-auto mx-auto">
		<TaskList title="To Do" />
		<TaskList title="In Progress" />
		<TaskList title="Done" />
	</div>
</div>
</template>