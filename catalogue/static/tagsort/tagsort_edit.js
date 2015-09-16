!function(e){
	e.fn.tagSort=function(t){
		var a={
			selector:".item-tagsort",
			tagWrapper:"span",
			displaySelector:!1,
			displaySeperator:" ",
			inclusive:!1,
			fadeTime:200
		};
		t=e.extend(a,t);
		var n={
			generateTags:function(a){
				var i={},
				s={
					elements:[],
					tags:[]
				},
				r=e(document.createElement(t.tagWrapper));

				return a.each(function(){

					$element=e(this);

					var a=$element.data("item-tags"), 
					c=a.split(a.match(/,\s+/)?", ":",");

					e.each(c,function(e,a){
						var s=a.toLowerCase();

						i[s]||(i[s]=[],
							n.container.append(r.clone().text(a))),
							t.displaySelector!==!1&&$element.find(t.displaySelector).append(e>0?t.displaySeperator+a:a),
							i[s].push($element)
						}),
					s.elements.push($element),
					s.tags.push(c)}),
				1==t.inclusive?i:s
			}, 
			exclusiveSort:function(t){
				var a=[[],[]];
				return e.each(t.elements,function(i,s){
					var r=!0;n.container.find(".tagsort-active").each(function(){
						-1==t.tags[i].indexOf(e(this).text())&&(r=!1,a[0].push(s))
					}),
					1==r&&a[1].push(s)
				}),a
			},
			inclusiveSort:function(t){
				var a=[[],[]];
				return n.container.find(".tagsort-active").each(function(){
					e.each(t[e(this).text().toLowerCase()],function(e,t){
						a[1].push(t)
					})
				}),a
			},inititalize:function(a){
				n.container=a,
				n.container.addClass("tagsort-tags-container");
				var i=e(t.selector);
				n.tags=n.generateTags(i,n.container);
				var s=n.container.find(t.tagWrapper);
				s.click(function(){
					if(e(this).toggleClass("tagsort-active"), s.hasClass("tagsort-active")){
						i.fadeOut(t.fadeTime);
						var a=1==t.inclusive?n.inclusiveSort(n.tags,i):n.exclusiveSort(n.tags,i);
						a[0].length>0&&e.each(a[0],function(e,a){
							a.is(":visible")&&a.fadeOut(t.fadeTime)
						}),a[1].length>0&&e.each(a[1],function(e,a){
							a.is("visible")||a.fadeIn(t.fadeTime)
						})
					} else i.fadeIn(t.fadeTime)
				})
			}
		};
		return n.inititalize(this),e(this)
	}
}(jQuery);


















