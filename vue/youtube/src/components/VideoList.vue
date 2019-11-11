<template>
<ul class="list-group">
    <h2>영상 목록</h2>
    <VideoListItem v-for="video in videos" :key="video.id.videoId" :video="video" @video-select-event="selectedVideo"></VideoListItem>
    <!-- 부모 컴포넌트에서는 이벤트 listen(v-on) 
         원하는 메소드 실행 
    -->
</ul>
</template>

<script>
import VideoListItem from './VideoListItem'
export default {
    name: 'VideoList',
    components:{
        VideoListItem,
    },
    props: {
        videos: {
            type: Array,
            require: true
        }
    },
    methods: {
        selectedVideo(video) {
            this.$emit('video-select-event', video)
        }
    }
}
</script>

<style>

</style>