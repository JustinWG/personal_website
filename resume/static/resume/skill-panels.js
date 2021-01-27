const tabDataArray = JSON.parse(document.getElementById('skills-stars').textContent);

const bulletList = document.createElement('p');

if (tabDataArray) {
  const section = document.createElement('section');
  section.className = "journeyContainer";

  const header = document.createElement('div');
  header.className = "journeyHeader";

  const headerText = document.createTextNode("Skills");

  const tabs = document.createElement('div');
  tabs.className = "tabs";

  tabList = document.createElement('div');
  tabList.setAttribute('role', "tabList");
  tabList.setAttribute('aria-label', "Skills List");

  header.appendChild(headerText);
  section.appendChild(header);
  section.appendChild(tabs);
  tabs.appendChild(tabList);

  main = document.querySelector("div.main");
  main.appendChild(section);
}

tabDataArray.forEach(function(category) {

  tab = document.createElement('button');
  tab.setAttribute('role', 'tab');
  tab.setAttribute('aria-selected','false');
  tab.setAttribute('id', category.name);

  const tabName = document.createTextNode(category.name);

  tab.appendChild(tabName);
  tabList.appendChild(tab);

  tabPanel = document.createElement('div');
  tabPanel.setAttribute('role', 'tabPanelContent');
  tabPanel.setAttribute('aria-labelledby', category.name);
  tabPanel.hidden = true;

  category.skills.forEach(function(detail) {
    let lineItem = document.createElement('div');
    lineItem.setAttribute('role', 'tabPanelLine');
    lineItem.className ="grow";
    // lineItem.textContent = (detail.name + ' ' + detail.stars + '\r\n');
    lineItem.textContent = (detail.name +':' + '\xa0' + '\xa0' + '\xa0');
    let i = 0;
    for (i = 0; i < detail.stars; i++) {
      lineItem.textContent += '\u2605';
      }
    tabPanel.appendChild(lineItem)
  });

  document.querySelector('.tabs').appendChild(tabPanel);
});


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
