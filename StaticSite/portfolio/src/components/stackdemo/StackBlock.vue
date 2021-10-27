<template>
    <div class="outer" :class="dashed ? 'dashed-border' : ''">
        {{ icon }} {{ title }}
        <slot></slot>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    name: "StackBlock",
    props: {
        title: String,
        icon: String,
        vertical: Boolean,
        dashed: Boolean,
    }
})
</script>


<style lang="scss">
    .outer {
        border: 1px solid black;
        
        &.dashed-border {
            border: 1px dashed black;
        }
    }
</style>