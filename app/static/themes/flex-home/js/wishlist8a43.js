!function(i){"use strict";var t=function(i){window.showAlert("alert-success",i)},n=function(i){return window.trans=window.trans||{},"undefined"!==window.trans[i]&&window.trans[i]?window.trans[i]:i};window.showAlert=function(t,n){if(t&&""!==n){var a=Math.floor(1e3*Math.random()),s='<div class="alert '.concat(t,' alert-dismissible" id="').concat(a,'">\n                            <span class="close far fa-times" data-dismiss="alert" aria-label="close"></span>\n                            <i class="far fa-')+("alert-success"===t?"check":"times")+' message-icon"></i>\n                            '.concat(n,"\n                        </div>");i("#alert-container").append(s).ready((function(){window.setTimeout((function(){i("#alert-container #".concat(a)).remove()}),6e3)}))}},i(document).ready((function(){function a(){var t=decodeURIComponent(e("wishlist"));if(null!=t&&null!=t&&t){var n=JSON.parse(t),a=n.length;i(".wishlist-count").text(a),a>0&&(i(".add-to-wishlist").removeClass("far fa-heart"),i.each(n,(function(t,n){null!=n&&i(document).find(".add-to-wishlist[data-id=".concat(n.id,"] i")).addClass("fas fa-heart")})))}}function s(i,t,n){var a=new Date,s=window.siteUrl;s.includes(window.location.protocol)||(s=window.location.protocol+s);var e=new URL(s.html);a.setTime(a.getTime()+24*n*60*60*1e3);var o="expires="+a.toUTCString();document.cookie=i+"="+t+"; "+o+"; path=/; domain="+e.hostname}function e(i){for(var t=i+"=",n=document.cookie.split(";"),a=0;a<n.length;a++){for(var s=n[a];" "==s.charAt(0);)s=s.substring(1);if(0==s.indexOf(t))return s.substring(t.length,s.length)}return""}function o(i){var t=window.siteUrl;t.includes(window.location.protocol)||(t=window.location.protocol+t);var n=new URL(t.html);document.cookie=i+"=; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/; domain="+n.hostname}a(),i(document).on("click",".add-to-wishlist",(function(d){d.preventDefault();var r="wishlist",l=i(this).data("id"),c=decodeURIComponent(e(r)),f=[];if(null!=l&&0!=l&&null!=l)if(null==c||null==c||""==c){var u={id:l};f.push(u),i(".add-to-wishlist[data-id=".concat(l,"] i")).removeClass("far fa-heart").addClass("fas fa-heart"),t(n("Added to wishlist successfully!")),s(r,JSON.stringify(f),60)}else{var w={id:l},h=(f=JSON.parse(c)).map((function(i){return i.id})).indexOf(w.id);-1===h?(f.push(w),o(r),s(r,JSON.stringify(f),60),i(".add-to-wishlist[data-id=".concat(l,"] i")).removeClass("far fa-heart").addClass("fas fa-heart"),t(n("Added to wishlist successfully!"))):(f.splice(h,1),o(r),s(r,JSON.stringify(f),60),i(".add-to-wishlist[data-id=".concat(l,"] i")).removeClass("fas fa-heart").addClass("far fa-heart"),t(n("Removed from wishlist successfully!")))}var m=JSON.parse(e(r)).length;i(".wishlist-count").text(m),a()})),i(document).on("click",".remove-from-wishlist",(function(d){d.preventDefault();var r="wishlist",l=i(this).data("id"),c=decodeURIComponent(e(r)),f=[];if(null!=l&&0!=l&&null!=l){var u={id:l},w=(f=JSON.parse(c)).map((function(i){return i.id})).indexOf(u.id);-1!=w&&(f.splice(w,1),o(r),s(r,JSON.stringify(f),60),t(n("Removed from wishlist successfully!")),i(".wishlist-page .item[data-id=".concat(l,"]")).closest("div").remove())}var h=JSON.parse(e(r)).length;i(".wishlist-count").text(h),a()})),window.wishlishInElement=function(t){var n=JSON.parse(e("wishlist")||"{}");n&&n.length&&t.find(".add-to-wishlist").map((function(){var t=i(this).data("id");n.some((function(i){return i.id===t}))&&i(this).find("i").addClass("fas")}))}}))}(jQuery);