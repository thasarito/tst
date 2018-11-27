<div>
  <div class="search-container">
      <input type="text" placeholder="ค้นหา.." v-model="live_search" aria-label="Search">
  </div>
  <div class="card animated slideInUp" v-for="word in words">
    <div class="score">
      <a v-on:click="Vote(word.id, 'up')">
        
      <i class="fal fa-hand-point-up"></i>
      [[ word.up ]]
      </a>
      <a v-on:click="Vote(word.id, 'down')">
        [[ word.down ]]
        <i class="fal fa-hand-point-down"></i>
      
      </a>
    </div>
    <div class="text">
      <a  v-bind:href="word.url">[[ word.name ]]</a><span> แปลว่า</span>
      <p>[[ word.meaning ]]</p>
    </div>
  </div>
  <div class="load-more animated slideInUp" v-on:click="loadMore()" v-if="more"><p>เพิ่มเติม...<i class="fal fa-chevron-double-down"></i></p></div>
  <h1 class="end" v-if="end"><i class="fal fa-empty-set"></i></h1>
  <div id="add" v-on:click="toggleModal()"><i class="fas fa-plus-circle"></i></div>
  <!-- div addWord Modal -->
  <transition name="fade" enter-active-class="animated zoomInUp faster"  leave-active-class="animated zoomOut faster">
    <div id="add-modal" class="modal" v-if="showModal" v-on:click.self="toggleModal()">
      <div class="add-modal-content">
        <form action="" v-on:submit.prevent="addWords()">
        <div class="name">
          <label for="">คำศัพท์</label>
          <input type="text" v-model="newWord.name">
        </div>
        <div class="readas">
          <label for="">อ่านว่า</label>
          <input type="text" v-model="newWord.readas">
        </div>
        <div class="meaning">
          <label for="">แปลว่า</label>
          <textarea type="text" v-model="newWord.meaning"></textarea>
        </div>
        <button>Submit</button>
        </form>
      </div>
    </div>
  </transition>
  <!-- end addWord Modal -->
</div>