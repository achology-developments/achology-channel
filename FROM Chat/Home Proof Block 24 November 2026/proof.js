(function () {
	var sec = document.getElementById('home-proof'); if (!sec) return;
	var still = matchMedia('(prefers-reduced-motion: reduce)').matches, held = 0;
	function shown() { return [].slice.call(sec.querySelectorAll('.hpp-col .pfp-rv:not(.is-held)')); }
	// The room every card holds only grows, so a longer review never makes the block jump back and forth.
	function room() {
		var cs = shown();
		cs.forEach(function (c) { c.style.minHeight = ''; });
		cs.forEach(function (c) { held = Math.max(held, Math.ceil(c.getBoundingClientRect().height)); });
		if (matchMedia('(min-width: 1024px)').matches) cs.forEach(function (c) { c.style.minHeight = held + 'px'; });
	}
	sec.addEventListener('click', function (e) {
		var out = e.target.closest('.hpp-col .pfp-rv'); if (!out || out.dataset.busy) return;
		var col = out.parentNode, next = col.querySelector('.pfp-rv.is-held'); if (!next) return;
		out.dataset.busy = '1'; out.classList.add('is-fading');
		setTimeout(function () {
			out.classList.remove('is-fading'); out.classList.add('is-held'); delete out.dataset.busy;
			col.appendChild(out);              /* it goes to the back of its stage's ten */
			next.classList.remove('is-held');
			room();
			if (!still) { next.classList.add('is-glowing'); setTimeout(function () { next.classList.remove('is-glowing'); }, 1700); }
			var b = next.querySelector('.pfp-rv__lab'); if (b && out.contains(document.activeElement) === false && e.detail === 0) b.focus({ preventScroll: true });
		}, still ? 0 : 260);
	});
	window.addEventListener('resize', function () { held = 0; room(); });
	if (document.fonts && document.fonts.ready) document.fonts.ready.then(room); else room();
})();
