const f1Memes = [
    {
        id: 1,
        title: "When your teammate beats your lap time",
        desc: "That moment when your teammate just edges you out in qualifying",
        gifUrl: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjVqZW96MXhubDY4ZmYzbnY5MTExamFhOHY4MHhjY2Q4cTk0a2EweiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/oDSzlVeXHLsIg/giphy.gif",
        tags: ["driver", "qualifying", "team"]
    },
    {
        id: 2,
        title: "Radio messages be like",
        desc: "When the team gives you confusing instructions during the race",
        gifUrl: "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmNvY3dxNGRlbWhkbmc4aHZucXBqN2VoczluYW1oYzJmYmhkdXMzaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ehTz6odmTnLhSifWml/giphy.gif",
        tags: ["radio", "team", "funny"]
    },
    {
        id: 3,
        title: "Hamilton vs Verstappen battle",
        desc: "The intense battles we've seen between these two champions",
        gifUrl: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExejV6dDVzMWs3Nm9jZzg3bG02Y3FhYXN2aWo4bnRsNXg4ZHg4cmNwNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ZLGc8xQXdXvvrwRfe6/giphy.gif",
        tags: ["battle", "champions", "rivalry"]
    },
    {
        id: 4,
        title: "Pit stop gone wrong",
        desc: "When the pit stop doesn't go as planned",
        gifUrl: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGEyamM0eWhyOG54N2RqM2h1ZWRrZ3RkdG40bHV3cTkwbG12bXcwayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/DN0VIGdNuIhGpO1TQP/giphy.gif",
        tags: ["pitstop", "fail", "team"]
    },
    {
        id: 5,
        title: "Ferrari strategy meeting",
        desc: "How we imagine Ferrari's strategy meetings go",
        gifUrl: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZTNqaHp5dDhlcjd0amp1ODRzajcwdGJ0NmY3MmVsemo1N3EwZW1wMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/nCqAmGyY7TzouggFSp/giphy.gif",
        tags: ["ferrari", "strategy", "funny"]
    },
    {
        id: 6,
        title: "When you finally get points",
        desc: "That feeling when a smaller team finally scores points",
        gifUrl: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWVjcGVyczMwbHpieGkzY2ZrNzc0d2VpbG5qaGh5ajd3YWRoY3l3aSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0ISCUDmAgGmlOjC/giphy.gif",
        tags: ["celebration", "points", "team"]
    },
    {
        id: 7,
        title: "Start line chaos",
        desc: "The chaos that sometimes happens at the race start",
        gifUrl: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHpuZDJldGtqdnp0b3pidnhtd3JxbW9ndnF4am8zb3BvNHVrOG9weSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/TgHQOqCqf9GH6/giphy.gif",
        tags: ["start", "chaos", "race"]
    },
    {
        id: 8,
        title: "Post-race interview face",
        desc: "That forced smile after a tough race",
        gifUrl: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjA2em1rZm1xaXFudXN6eW5zdmg3eTgyYzdnZHV5andvdzRjanIzbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/2N4il6lyCGBQXEfCHr/giphy.gif",
        tags: ["interview", "driver", "funny"]
    }
];

// Pagination
const MEMES_PER_PAGE = 4;
let currentPage = 0;
let filteredMemes = [...f1Memes];
let selectedTags = [];

// DOM Elements
const memesGrid = document.getElementById('memes-grid');
const loader = document.getElementById('loader');
const filterTagsContainer = document.getElementById('filter-tags');
const loadMoreBtn = document.getElementById('load-more-btn');
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');

// Get all unique tags
function getAllTags() {
    const tagsSet = new Set();
    f1Memes.forEach(meme => {
        meme.tags.forEach(tag => tagsSet.add(tag));
    });
    return Array.from(tagsSet).sort();
}

// Render filter buttons
function renderFilterTags() {
    const allTags = getAllTags();
    filterTagsContainer.innerHTML = '';

    const clearBtn = document.createElement('button');
    clearBtn.className = 'filter-btn active';
    clearBtn.textContent = 'All';
    clearBtn.addEventListener('click', () => {
        selectedTags = [];
        currentPage = 0;
        filterAndRender();
        updateFilterButtons();
    });
    filterTagsContainer.appendChild(clearBtn);

    allTags.forEach(tag => {
        const btn = document.createElement('button');
        btn.className = 'filter-btn';
        btn.textContent = tag.charAt(0).toUpperCase() + tag.slice(1);
        btn.addEventListener('click', () => {
            const index = selectedTags.indexOf(tag);
            if (index > -1) {
                selectedTags.splice(index, 1);
            } else {
                selectedTags.push(tag);
            }
            currentPage = 0;
            filterAndRender();
            updateFilterButtons();
        });
        filterTagsContainer.appendChild(btn);
    });
}

// Update filter button active states
function updateFilterButtons() {
    const buttons = document.querySelectorAll('.filter-btn');
    buttons.forEach((btn, index) => {
        if (index === 0) {
            btn.classList.toggle('active', selectedTags.length === 0);
        } else {
            btn.classList.toggle('active', selectedTags.includes(btn.textContent.toLowerCase()));
        }
    });
}

// Filter memes based on selected tags
function filterAndRender() {
    if (selectedTags.length === 0) {
        filteredMemes = [...f1Memes];
    } else {
        filteredMemes = f1Memes.filter(meme =>
            selectedTags.some(tag => meme.tags.includes(tag))
        );
    }
    renderMemes();
    updateLoadMoreButton();
}

// Function to render memes with pagination
function renderMemes() {
    const startIndex = currentPage * MEMES_PER_PAGE;
    const endIndex = startIndex + MEMES_PER_PAGE;
    const memesToDisplay = filteredMemes.slice(0, endIndex);

    memesGrid.innerHTML = '';

    if (memesToDisplay.length === 0) {
        memesGrid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; color: #999; padding: 40px;">No memes found with selected filters.</p>';
        loadMoreBtn.style.display = 'none';
        return;
    }

    memesToDisplay.forEach(meme => {
        const memeCard = document.createElement('div');
        memeCard.className = 'meme-card';

        let tagsHTML = '';
        meme.tags.forEach(tag => {
            const tagClass = tag === 'driver' ? 'driver' : (tag === 'team' ? 'team' : '');
            tagsHTML += `<span class="tag ${tagClass}">${tag}</span>`;
        });

        memeCard.innerHTML = `
            <img src="${meme.gifUrl}" alt="${meme.title}" class="meme-img" data-meme-id="${meme.id}">
            <div class="meme-info">
                <h3 class="meme-title">${meme.title}</h3>
                <p class="meme-desc">${meme.desc}</p>
                <div class="meme-tags">
                    ${tagsHTML}
                </div>
            </div>
        `;

        memesGrid.appendChild(memeCard);
    });

    // Add error handling for images
    document.querySelectorAll('.meme-img').forEach(img => {
        img.addEventListener('error', function () {
            this.style.display = 'none';
            const placeholder = document.createElement('div');
            placeholder.className = 'meme-img-placeholder';
            placeholder.innerHTML = '<i class="fas fa-image"></i> Image not available';
            this.parentNode.insertBefore(placeholder, this);
        });
        img.addEventListener('load', function () {
            this.style.display = 'block';
        });
    });
}

// Update Load More button visibility
function updateLoadMoreButton() {
    const totalDisplayed = Math.min((currentPage + 1) * MEMES_PER_PAGE, filteredMemes.length);
    if (totalDisplayed < filteredMemes.length) {
        loadMoreBtn.style.display = 'block';
    } else {
        loadMoreBtn.style.display = 'none';
    }
}

// Load more memes
function loadMore() {
    currentPage++;
    renderMemes();
    updateLoadMoreButton();
    memesGrid.scrollIntoView({ behavior: 'smooth' });
}

// Toggle hamburger menu
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('show');
});

// Close menu when link is clicked
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        hamburger.classList.remove('active');
        navMenu.classList.remove('show');

        document.querySelectorAll('nav a').forEach(item => {
            item.classList.remove('active');
        });
        this.classList.add('active');
    });
});

// Load more button event listener
loadMoreBtn.addEventListener('click', loadMore);

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
    renderFilterTags();
    renderMemes();
    updateLoadMoreButton();
});