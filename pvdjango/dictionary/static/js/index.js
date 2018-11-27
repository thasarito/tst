const api_url = '/api/description/'
var vm = new Vue ({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    words: [],
    curWord: {},
    nextPageUrl: null
  },

  mounted: function () {
    this.getWords();
  },

  methods: {
    getWords: function () {
      this.$http.get(api_url)
      .then((response) => {
        this.words = response.data.results
        this.nextPageUrl = response.data.next
      })
    }
  }
})