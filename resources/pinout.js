const content = document.querySelector('main')
const gpio = document.querySelector('#gpio')
const view = document.querySelector('#pinout-view')

const pinNav = (pin, suffix = '') => document.querySelectorAll(`#gpio li.pin${pin} ${suffix}`)

const activate = (tab, focus) => {
	const group = tab.closest('.pin-function-tabs')

	for (const other of group.querySelectorAll('[role="tab"]')) {
		other.setAttribute('aria-selected', other === tab)
		other.tabIndex = other === tab ? 0 : -1
	}

	for (const panel of group.querySelectorAll('[role="tabpanel"]')) {
		panel.hidden = panel.id !== tab.getAttribute('aria-controls')
	}

	if (focus) {
		tab.focus()
	}
}

for (const group of document.querySelectorAll('.pin-function-tabs')) {
	const tabs = group.querySelectorAll('[role="tab"]')

	if (!tabs.length) {
		continue
	}

	group.classList.add('tabbed')
	group.querySelector('.tabs').hidden = false
	activate(group.querySelector('[role="tab"][aria-selected="true"]') ?? tabs[0], false)
}

for (const block of document.querySelectorAll('pre')) {
	block.classList.add('prettyprint', 'linenums')
}

window.prettyPrint?.()

content?.addEventListener('click', event => {
	const tab = event.target.closest('[role="tab"]')

	if (tab) {
		activate(tab, false)
		return
	}

	const reference = event.target.closest('article .pin-hover')
	const link = reference && pinNav(reference.dataset.pin, 'a')[0]

	if (link) {
		window.location = link.href
	}
})

content?.addEventListener('keydown', event => {
	const step = {ArrowRight: 1, ArrowLeft: -1}[event.key]
	const tab = step && event.target.closest('[role="tab"]')

	if (!tab) {
		return
	}

	const tabs = [...tab.closest('.pin-function-tabs').querySelectorAll('[role="tab"]')]
	activate(tabs[(tabs.indexOf(tab) + step + tabs.length) % tabs.length], true)
})

const highlight = (event, hovered) => {
	const reference = event.target.closest('article .pin-hover')

	if (!reference) {
		return
	}

	for (const item of pinNav(reference.dataset.pin)) {
		item.classList.toggle('hover-pin', hovered)
	}
}

content?.addEventListener('mouseover', event => highlight(event, true))
content?.addEventListener('mouseout', event => highlight(event, false))

view?.removeAttribute('hidden')

view?.addEventListener('click', event => {
	const button = event.target.closest('button')

	if (!button) {
		return
	}

	const mode = button.classList.contains('mirror') ? 'mirror' : 'rotate'
	const pressed = !gpio.classList.contains(mode)

	gpio.classList.toggle(mode, pressed)
	gpio.classList.remove('flipping', 'rotating', 'rotating-back')
	void gpio.offsetWidth
	gpio.classList.add(mode === 'mirror' ? 'flipping' : 'rotating')

	if (mode === 'rotate' && !pressed) {
		gpio.classList.add('rotating-back')
	}

	button.setAttribute('aria-pressed', pressed)
})

gpio?.addEventListener('animationend', event => {
	if (event.target === gpio) {
		gpio.classList.remove('flipping', 'rotating', 'rotating-back')
	}
})
