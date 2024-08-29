// ==UserScript==
// @name         Codecademy Ad and Prompt Blocker
// @namespace    http://tampermonkey.net/
// @version      1.1
// @description  Block certain ads and prompts on Codecademy website
// @author       Your Name
// @match        https://www.codecademy.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Function to remove element by checking its child nodes
    function removeElementIfChildMatches(parentElement, childTag, childText, exactMatch = true) {
        if (parentElement) {
            const childElement = parentElement.querySelector(childTag);
            if (childElement && (
                exactMatch ? childElement.textContent.trim() === childText :
                childElement.textContent.includes(childText)
            )) {
                parentElement.remove();
            }
        }
    }

    // Function to search and remove unwanted elements
    function removeUnwantedElements() {
        // 1. Check for the element with data-testid="overlay-content-container"
        const overlayContentContainer = document.querySelector('[data-testid="overlay-content-container"]');
        removeElementIfChildMatches(overlayContentContainer, 'h2', 'Update your payment method');

        // 2. Check for the element with aria-label="alert banner"
        const alertBanner = document.querySelector('[aria-label="alert banner"]');
        removeElementIfChildMatches(alertBanner, 'span', 'Please verify your email so we can make sure your account is secure.', false);
    }

    // Initial check when the script first runs
    removeUnwantedElements();

    // Create a MutationObserver to watch for changes in the DOM
    const observer = new MutationObserver(() => {
        removeUnwantedElements();
    });

    // Start observing the document body for added/removed child elements
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

})();
