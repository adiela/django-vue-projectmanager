<template>
    <div class="relative flex flex-col items-start p-4 mt-3 bg-white rounded-lg cursor-pointer bg-opacity-90 group hover:bg-opacity-100 shadow-md w-72" draggable="true">
            <button class="absolute top-0 right-0 flex items-center justify-center hidden w-5 h-5 mt-3 mr-2 text-gray-500 rounded hover:bg-gray-200 hover:text-gray-700 group-hover:flex">
                <svg class="w-4 h-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
                </svg>
            </button>
            <span class="flex items-center h-6 px-3 text-xs font-semibold text-pink-500 bg-pink-100 rounded-full">{{ this.task.tag }}</span>
            <h4 class="mt-3 text-sm font-medium">{{ this.task.title }}</h4>
            <div class="flex items-center w-full mt-3 text-xs font-medium text-gray-400">
                <div class="flex items-center">
                    <svg class="w-4 h-4 text-gray-300 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
                    </svg>
                    <span class="ml-1 leading-none">{{ this.task.due_date }}</span>
                </div>
                <div class="relative flex items-center ml-4">
                    <svg class="relative w-4 h-4 text-gray-300 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z" clip-rule="evenodd" />
                    </svg>
                    <span class="ml-1 leading-none">{{ this.task.comment_count }}</span>
                </div>
                <div class="ml-auto flex">
                    <img v-if="this.task.assignees.length == 1" class="w-6 h-6 rounded-full" :src="this.task.assignees[0].avatar" />
                    <img v-if="this.task.assignees.length > 1" v-for="assignee in this.task.assignees" class="w-6 h-6 -ml-2.5 rounded-full" :src="assignee.avatar" />
                </div>
                
            </div>
        </div>
</template>

<script>
export default {
    name: 'TaskCard',
    props: {
        task: {
            type: Object,
            required: true
        }
    }
}
</script>