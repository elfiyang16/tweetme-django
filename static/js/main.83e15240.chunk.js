(this["webpackJsonptweetme-web"]=this["webpackJsonptweetme-web"]||[]).push([[0],[,,,,,,,function(e,t,a){e.exports=a(15)},,,,,function(e,t,a){},function(e,t,a){e.exports=a.p+"static/media/logo.5d5d9eef.svg"},function(e,t,a){},function(e,t,a){"use strict";a.r(t);var n=a(0),c=a.n(n),r=a(4),o=a.n(r),s=(a(12),a(13),a(14),a(5)),l=a(1);function i(e){var t=Object(n.useState)([]),a=Object(l.a)(t,2),r=a[0],o=a[1],i=Object(n.useState)([]),m=Object(l.a)(i,2),p=m[0],d=m[1];return Object(n.useEffect)((function(){var t=Object(s.a)(e.newTweets).concat(r);t.length!==p.length&&d(t)}),[e.newTweets,p,r]),Object(n.useEffect)((function(){!function(e){var t=new XMLHttpRequest;t.responseType="json",t.open("GET","http://localhost:8000/api/tweets/"),t.onload=function(){e(t.response,t.status)},t.onerror=function(t){console.log(t),e({message:"The request was an error"},400)},t.send()}((function(e,t){200===t?o(e):alert("There was an error")}))}),[r]),p.map((function(e,t){return c.a.createElement(u,{tweet:e,className:"my-5 py-5 border bg-white text-dark",key:"".concat(t,"-{item.id}")})}))}function m(e){var t=e.tweet,a=e.action,r=Object(n.useState)(t.likes?t.likes:0),o=Object(l.a)(r,2),s=o[0],i=o[1],m=Object(n.useState)(!0===t.userLike),u=Object(l.a)(m,2),p=u[0],d=u[1],f=e.className?e.className:"btn btn-primary btn-sm",w=a.display?a.display:"Action",b="like"===a.type?"".concat(s," ").concat(w):w;return c.a.createElement("button",{className:f,onClick:function(e){e.preventDefault(),"like"===a.type&&(!0===p?(i(s-1),d(!1)):(i(s+1),d(!0)))}},b)}function u(e){var t=e.tweet,a=e.className?e.className:"col-10 mx-auto col-md-6";return c.a.createElement("div",{className:a},c.a.createElement("p",null,t.id," - ",t.content),c.a.createElement("div",{className:"btn btn-group"},c.a.createElement(m,{tweet:t,action:{type:"like",display:"Likes"}}),c.a.createElement(m,{tweet:t,action:{type:"unlike",display:"Unlike"}}),c.a.createElement(m,{tweet:t,action:{type:"retweet",display:""}})))}function p(e){var t=Object(n.useState)([]),a=Object(l.a)(t,2),r=a[0],o=a[1],m=c.a.createRef();return c.a.createElement("div",{className:e.className},c.a.createElement("div",{className:"col-12 mb-3"},c.a.createElement("form",{onSubmit:function(e){e.preventDefault();var t=m.current.value,a=Object(s.a)(r);a.unshift({content:t,likes:0,id:12313}),o(a),m.current.value=""}},c.a.createElement("textarea",{ref:m,required:!0,className:"form-control",name:"tweet"}),c.a.createElement("button",{type:"submit",className:"btn btn-primary my-3"},"Tweet"))),c.a.createElement(i,{newTweets:r}))}var d=function(){return c.a.createElement("div",{className:"App"},c.a.createElement("header",{className:"App-header"},c.a.createElement(p,null)))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var f=document.getElementById("root");f&&o.a.render(c.a.createElement(d,null),f);var w=document.getElementById("tweetme-2");w&&o.a.render(c.a.createElement(p,null),w),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}],[[7,1,2]]]);
//# sourceMappingURL=main.83e15240.chunk.js.map