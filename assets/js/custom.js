function toggleCitation(id, event) {
  var popup = document.getElementById(id);
  var allPopups = document.getElementsByClassName('citation-popup');
  
  // Close all other popups
  for(var i = 0; i < allPopups.length; i++) {
    if(allPopups[i].id !== id) {
      allPopups[i].style.display = 'none';
    }
  }
  
  // Toggle this popup
  if(popup.style.display === 'block') {
    popup.style.display = 'none';
  } else {
    popup.style.display = 'block';
    
    // Position the popup
    var evt = event || window.event;
    var btn = evt && evt.currentTarget ? evt.currentTarget : evt && evt.target ? evt.target : null;
    if (!btn) {
      return;
    }
    var btnRect = btn.getBoundingClientRect();
    var popupRect = popup.getBoundingClientRect();
    
    // Calculate position to show below the button
    var top = btnRect.bottom + window.scrollY + 10;
    var left = btnRect.left + window.scrollX - (popupRect.width / 2) + (btnRect.width / 2);
    
    // Ensure popup stays within viewport
    if (left < 10) left = 10;
    if (left + popupRect.width > window.innerWidth - 10) 
      left = window.innerWidth - popupRect.width - 10;
    
    popup.style.top = top + 'px';
    popup.style.left = left + 'px';
  }
}

function copyToClipboard(text, btnElement) {
  navigator.clipboard.writeText(text).then(function() {
    // Store original text
    var originalText = btnElement.textContent;
    
    // Update button text
    btnElement.textContent = "已复制!";
    if (document.documentElement.lang !== 'zh') {
      btnElement.textContent = "Copied!";
    }
    
    // Reset button text after a delay
    setTimeout(function() {
      btnElement.textContent = originalText;
    }, 1500);
  }, function(err) {
    console.error('Could not copy text: ', err);
    alert('Failed to copy');
  });
}

// Close popups when clicking outside
window.onclick = function(event) {
  if (!event.target.matches('.citation-trigger') && 
      !event.target.closest('.citation-trigger') && 
      !event.target.closest('.citation-popup') && 
      !event.target.matches('.copy-btn')) {
    var popups = document.getElementsByClassName('citation-popup');
    for(var i = 0; i < popups.length; i++) {
      popups[i].style.display = 'none';
    }
  }
}

// Initialize after DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
  // Create copy buttons for citation formats
  var citationFormats = document.querySelectorAll('.citation-format');
  citationFormats.forEach(function(format) {
    var citationText = format.innerText.trim();
    format.setAttribute('data-citation-text', citationText);
    var copyBtn = document.createElement('button');
    copyBtn.className = 'copy-btn';
    copyBtn.textContent = document.documentElement.lang === 'zh' ? '复制' : 'Copy';
    copyBtn.onclick = function(e) {
      e.stopPropagation();
      copyToClipboard(format.getAttribute('data-citation-text') || format.textContent, this);
    };
    format.appendChild(copyBtn);
  });
}); 
