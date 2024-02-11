export async function getActiveTabURL() {
  const tabs = await chrome.tabs.query({
    currentWindow: true,
    active: true,
  });
  console.log(tabs[0]);
  return tabs[0];
}
