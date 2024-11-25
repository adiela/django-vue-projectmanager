<template>
<div class="flex flex-col w-screen text-gray-700 bg-gradient-to-tr from-blue-200 via-indigo-200 to-pink-200 py-10 min-h-screen">
	<div class="px-10 mt-6">
		<h1 class="text-3xl font-bold text-center">Team Project Board</h1>
	</div>
	<div class="flex flex-grow px-10 mt-4 space-x-6 overflow-x-auto mx-auto">
		<TaskList title="To Do" :tasks="toDoTasks" />
		<TaskList title="In Progress" :tasks="inProgressTasks" />
		<TaskList title="Done" :tasks="doneTasks" />
	</div>
</div>
</template>

<script>
import TaskList from '~/components/TaskList.vue'

export default {
	components: {
		TaskList
	},
	data() {
		return {
			tasks: [
				{
					id: 1,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Design',
					due_date: 'Dec 12',
					comment_count: 2,
					assignees: [
						{
							name: 'John Doe',
							avatar: 'https://randomuser.me/api/portraits/men/75.jpg',
							
						},
						{
							name: 'Jane Doe',
							avatar: 'https://randomuser.me/api/portraits/women/26.jpg',
						}
					],
					status: 'To Do'
				},	
				{
					id: 2,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Design',
					due_date: 'Dec 12',
					comment_count: 6,
					assignees: [
						{
							name: 'John Doe',
							avatar: 'https://randomuser.me/api/portraits/men/75.jpg',
							
						},
						{
							name: 'Jane Doe',
							avatar: 'https://randomuser.me/api/portraits/women/26.jpg',
						}
					],
					status: 'In Progress'
				},
				{
					id: 3,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Development',
					due_date: 'Dec 15',
					comment_count: 4,
					assignees: [
						{
							name: 'John Doe',
							avatar: 'https://randomuser.me/api/portraits/men/75.jpg',
							
						},
						{
							name: 'Jane Doe',
							avatar: 'https://randomuser.me/api/portraits/women/26.jpg',
						}
					],
					status: 'Done'
				},
				{
					id: 4,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Development',
					due_date: 'Dec 16',
					comment_count: 0,
					assignees: [],
					status: 'To Do'
				},
				{
					id: 5,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Design',
					due_date: 'Dec 12',
					comment_count: 4,
					assignees: [
						{
							name: 'John Doe',
							avatar: 'https://randomuser.me/api/portraits/men/75.jpg',
							
						},
						{
							name: 'Jane Doe',
							avatar: 'https://randomuser.me/api/portraits/women/26.jpg',
						}
					],
					status: 'In Progress'
				},
				{
					id: 6,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Testing',
					due_date: 'Dec 18',
					comment_count: 4,
					assignees: [
						{
							name: 'John Doe',
							avatar: 'https://randomuser.me/api/portraits/men/75.jpg',
							
						},
						{
							name: 'Jane Doe',
							avatar: 'https://randomuser.me/api/portraits/women/26.jpg',
						}
					],
					status: 'Done'
				},
				{
					id: 7,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Testing',
					due_date: 'Dec 18',
					comment_count: 4,
					assignees: [
						{
							name: 'John Doe',
							avatar: 'https://randomuser.me/api/portraits/men/75.jpg',
							
						},
					],
					status: 'To Do'
				},
				{
					id: 8,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Testing',
					due_date: 'Dec 18',
					comment_count: 10,
					assignees: [
						{
							name: 'John Doe',
							avatar: 'https://randomuser.me/api/portraits/men/75.jpg',
							
						},
						{
							name: 'Jane Doe',
							avatar: 'https://randomuser.me/api/portraits/women/26.jpg',
						}
					],
					status: 'In Progress'
				},
				{
					id: 9,
					title: 'This is the title of the card for the thing that needs to be done.',
					tag: 'Launch',
					due_date: 'Dec 18',
					comment_count: 12,
					assignees: [
						{
							name: 'John Doe',
							avatar: 'https://randomuser.me/api/portraits/men/75.jpg',
							
						},
						{
							name: 'Jane Doe',
							avatar: 'https://randomuser.me/api/portraits/women/26.jpg',
						}
					],
					status: 'In Progress'
				},
			]
		}
	},
	computed: {
		toDoTasks() {
			return this.tasks.filter(task => task.status === 'To Do')
		},
		inProgressTasks() {
			return this.tasks.filter(task => task.status === 'In Progress')
		},
		doneTasks() {
			return this.tasks.filter(task => task.status === 'Done')
		},
	},
	methods: {
		dragStart(event) {
			event.dataTransfer.setData('text/plain', event.target.id)
		},
		dragOver(event) {
			event.preventDefault()
		},
		drop(event) {
			event.preventDefault()
			const id = event.dataTransfer.getData('text/plain')
			const draggableElement = document.getElementById(id)
			const dropzone = event.target
			dropzone.appendChild(draggableElement)
		}
	}
}

</script>