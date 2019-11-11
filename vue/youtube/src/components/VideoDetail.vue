<template>
<div v-if="video">
  <h3>비디오</h3>
  <iframe :src="videoUrl" width="560" height="315" framborder="0"></iframe>
</div>
</template>

<script>
export default {
    name: 'VideoDetail',
    props:{
        video: {
            type: Object,
            //requried: true 초기에 선택이 되어 있지 않을 수 있으므로
        }
    },
    computed: {
        videoUrl() {
            return `https://www.youtube.com/embed/${this.video.id.videoId}`
        }
    }
}
</script>

<style>

</style>