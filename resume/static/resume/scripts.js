const tabs = document.querySelector('.tabs');
const tabButtons = tabs.querySelectorAll('[role="tab"]');
const tabPanels = Array.from(tabs.querySelectorAll('[role="tabPanelContent"]'));

function handleTabClick(e) {
  // hide all tabPanels
  tabPanels.forEach(panel => {
    panel.hidden = true;
  });

  // mark all tabs as unselected
  tabButtons.forEach(tab => {
    tab.setAttribute('aria-selected', false);
  });

  // mark the clicked tab as selected
  e.currentTarget.setAttribute('aria-selected', true);
  // show the associated tab panel
  const { id } = e.currentTarget;
  const tabPanel = tabPanels.find(panel => panel.getAttribute('aria-labelledby') === id);
  tabPanel.hidden = false;
}

// setting up the initial look of the site: placing listeners and activating first skills tab
tabButtons.forEach(button => button.addEventListener('click', handleTabClick));
tabButtons.forEach(button => button.setAttribute('aria-selected', false));
tabButtons.item(0).setAttribute('aria-selected', true);
tabPanels[0].hidden = false;
