Vue.component('word-list', {
  delimiters: ['[[', ']]'],
	template: `
  <div class="card animated slideInUp">
    <div class="score">
      <a v-on:click="">
        
      <i class="fal fa-hand-point-up"></i>
      [[ word.up ]]
      </a>
      <a v-on:click="">
        [[ word.down ]]
        <i class="fal fa-hand-point-down"></i>
      
      </a>
    </div>
    <div class="text">
      <a  v-bind:href="word.url">[[ word.word.spelling ]]</a><span> แปลว่า</span>
      <p>[[ word.meaning ]]</p>
    </div>
  </div>
  `,
  data: function () {
    return {

    }
  },

  props: {
    word: {}
  },

  methods: {
    Vote: function () {

    }
  }
})

