!function(e){
	e.fn.tagSort=function(t){ 
	  // Deze regel defineert de tagSort() functie als een jQuery functie. Hier mee kan je dus $.tagSort() oproepen in je eigen scripts
	  
		var a={ // a: init params

			selector:".item-tagsort", // default waarde voor de css klasse die een tagsort item aangeeft
			tagWrapper:"span", // tags will be wrapped in <span> elements
			displaySelector:!1, // false
			displaySeperator:" ", // seperator voor tags?
			inclusive:!1, // false
			fadeTime:200
		};

		t=e.extend(a,t); // jQuery extend() function: merge the content of two or more objects together into the first object

		var n={
			generateTags:function(a){ // Deze funtie is verantwoordelijk voor het automatisch aanmaken van de tags
				
				var i={},

				s={ //dictionary
					elements:[],
					tags:[]
				},

				r=e(document.createElement(t.tagWrapper)); // JavaScript createElement function, dit maakt een <span> element aan

				return a.each(function(){ // jQuery each() function: itereer over jQuery object, waarbij de functie wordt uitgevoerd op elk element dat voldoet

					$element=e(this); // $element is het door jQuery geselecteerde element

					var a=$element.data("item-tags"), // Ga op zoek naar het html data attribuut 'data-item-tags'

					c=a.split(a.match(/,\s+/)?", ":","); // Split de waarde voor data-item-tags op volgens ':' of ','

					e.each(c,function(e,a){ // Voor elk van de tags uit de waarde van 'data-item-tags':
						var s=a.toLowerCase(); // Maak lowercase

						i[s]||(i[s]=[],n.container.append(r.clone().text(a))),
						t.displaySelector!==!1&&$element.find(t.displaySelector).append(e>0?t.displaySeperator+a:a),
						i[s].push($element)
					}),
					s.elements.push($element), // Voeg het element toe aan de dict
					s.tags.push(c) //Voeg de tag toe aan de dict
				}),
				1==t.inclusive?i:s // Check de inclusive parameter
			}, 

			exclusiveSort:function(t){ // Functie die wordt gebruik in geval van niet inclusive sort

				var a=[[],[]];

				return e.each(t.elements,function(i,s){
					var r=!0;n.container.find(".tagsort-active").each(function(){
						-1==t.tags[i].indexOf(e(this).text())&&(r=!1,a[0].push(s))
					}),
					1==r&&a[1].push(s)
				}), a
			},

			inclusiveSort:function(t){ // Functie die wordt gebruikt in geval van inclusive sort
				var a=[[],[]];
				return n.container.find(".tagsort-active").each(function(){
					e.each(t[e(this).text().toLowerCase()],function(e,t){
						a[1].push(t)
					})
				}), a
			},

			inititalize:function(a){

				n.container=a, 
				n.container.addClass("tagsort-tags-container"); 

				var i=e(t.selector); // De selector is de klasse die aan de items werd toegevoegd

				n.tags=n.generateTags(i,n.container); // 

				var s=n.container.find(t.tagWrapper); // 

				s.click(function(){

					if(e(this).toggleClass("tagsort-active"), s.hasClass("tagsort-active")){

						i.fadeOut(t.fadeTime); // jQuery fadeOut() functie: deze verbergt de element door ze te uit faden met de fadeTime parameter

						var a=1==t.inclusive?n.inclusiveSort(n.tags,i):n.exclusiveSort(n.tags,i);

						a[0].length>0&&e.each(a[0],function(e,a){

							a.is(":visible")&&a.fadeOut(t.fadeTime)

						}),a[1].length>0&&e.each(a[1],function(e,a){

							a.is("visible")||a.fadeIn(t.fadeTime)
						})
					} else i.fadeIn(t.fadeTime) // jQuery fadeIn() functie: omgekeerde van fadeOut()
				})
			}
		};
		return n.inititalize(this),e(this) // Initialiseer tagSort
	}
}(jQuery);


