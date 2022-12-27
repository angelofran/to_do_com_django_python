$(document).ready(function () {
   let baseUrl = 'http://127.0.0.1:8000/home/';
   let deleteBTN = $('.delete-btn');
   let searchbtn = $('#search-btn');
   let searchf = $('#search-form');
   var filter = $('#filter');
   $(deleteBTN).on('click', function (e) {
      e.preventDefault();
      let dellink = $(this).attr('href');
      let result = confirm('Quer deletar a tarefa?');
      if(result) {
         window.location.href = dellink
      }
   });
   $(searchbtn).on('click', function() {
      searchf.submit();
   });
   $(filter).change(function() {
      filter = $(this).val();
      window.location.href = baseUrl + '?filter=' + filter
   });
});
