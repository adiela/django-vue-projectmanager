<template>
<div class="flex flex-col flex-shrink-0">
    <div class="flex items-center flex-shrink-0 h-10 px-2">
        <span class="block text-sm font-semibold">{{ title }}</span>
        <span class="flex items-center justify-center w-5 h-5 ml-2 text-sm font-semibold text-indigo-500 bg-white rounded bg-opacity-30">{{ tasks.length }}</span>
        <button class="flex items-center justify-center w-6 h-6 ml-auto text-indigo-500 rounded hover:bg-indigo-500 hover:text-indigo-100">
            <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
        </button>
    </div>
    <div class="flex flex-col p-4">
        <TaskCard v-for="task in tasks" :task="task" :key="task.id" />
    </div>
</div>
</template>

<script>
import TaskCard from '~/components/TaskCard.vue'

export default {
    components: {
        TaskCard
    },
    props: {
        title: {
            type: String,
            required: true
        },
        tasks: {
            type: Array,
        }
    }
}
</script>