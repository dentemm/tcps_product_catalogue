;(function($) {
  $.fn.tagSort = function(options) {

      var defaults = { // Default settings
        selector: '.item-tagsort',
        tagWrapper: 'span',
        displaySelector: false,
        displaySeperator: ' ',
        inclusive: false, 
        fadeTime: 200
      };

      options = $.extend(defaults, options); // Gebruik de defaults als er geen options zijn 

      var tagSortEngine = { // De engine

        generateTags: function(elements) { // Generate Tags
          
          var tags_inclusive = {};
          var tags_exclusive = {elements: [], tags: []};

          var tagElement = $(document.createElement(options.tagWrapper)); // Maak een <span> element aan
          tagElement.addClass('btn btn-xs btn-pill btn-default m-l-xs m-y-xs');

          elements.each(function(i){ // Voor elk element:

            $element = $(this);


            var tagsData = $element.data('item-tags'), // Selecteer de tags, via het data attribute 'data-item-tags'
            elementTags = tagsData.match(/,\s+/) ? tagsData.split(', ') : tagsData.split(','); // De tags zelf zijn gescheiden door komma's
            
            $.each(elementTags, function(i, v){ 

              var tagName = v.toLowerCase();

              if(!tags_inclusive[tagName]){
                tags_inclusive[tagName] = [];
                tagSortEngine.container.append(tagElement.clone().text(v));
              }

              if(options.displaySelector !== false){
                $element.find(options.displaySelector).append(i > 0 ? options.displaySeperator + v : v);
              }

              tags_inclusive[tagName].push($element);
            });

            tags_exclusive.elements.push($element);
            tags_exclusive.tags.push(elementTags);
          });
          return options.inclusive == true ? tags_inclusive:tags_exclusive;
        },

        exclusiveSort: function(tags, elements){
          var display = [[],[]];
          $.each(tags.elements, function(element_key, element){
            var showElement = true;
            tagSortEngine.container.find('.active').each(function(i){
              if(tags.tags[element_key].indexOf($(this).text()) == -1){
                showElement = false;
                display[0].push(element);
              }
            });

            if(showElement == true) {
              display[1].push(element);
            }
          });
          return display;
        },

        inclusiveSort: function(tags, elements){
          var display = [[],[]]
          tagSortEngine.container.find('.active').each(function(i){
            $.each(tags[$(this).text().toLowerCase()],function(element_key, element){
              display[1].push(element);

            });
          });
          return display;
        },

        inititalize: function(tagsContainer){
          
          tagSortEngine.container = tagsContainer;
          tagSortEngine.container.addClass('tagsort-tags-container');
          var elements = $(options.selector);
          tagSortEngine.tags = tagSortEngine.generateTags(elements, tagSortEngine.container);
          var tagElement = tagSortEngine.container.find(options.tagWrapper);

          tagElement.click(function(){
            //$(this).toggleClass('tagsort-active');
            //if(!tagElement.hasClass('tagsort-active')){
            $(this).toggleClass('active');
            if(!tagElement.hasClass('active')) {
              elements.fadeIn(options.fadeTime);
            }
            else {
              elements.fadeOut(options.fadeTime);
              var display = options.inclusive == true ? tagSortEngine.inclusiveSort(tagSortEngine.tags, elements):tagSortEngine.exclusiveSort(tagSortEngine.tags, elements);
              if(display[0].length > 0){
                $.each(display[0], function(hide_key, toHide){
                  if(toHide.is(':visible')){
                    toHide.fadeOut(options.fadeTime);
                  }
                });
              }
              if(display[1].length > 0){
                $.each(display[1], function(hide_key, toShow){
                  if(!toShow.is('visible')){
                    toShow.fadeIn(options.fadeTime);
                  }
                });
              }
            }
          });
        }
      }
      tagSortEngine.inititalize(this);
      return $(this);
    }
})(jQuery);
