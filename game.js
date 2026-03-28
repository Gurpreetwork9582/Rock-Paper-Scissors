// Main Game Scene
class RockPaperScissorsScene extends Phaser.Scene {
    constructor() {
        super('RockPaperScissors');
    }

    preload() {
        // Load images from assets folder
        this.load.image('background', 'assets/Background.jpg');
        this.load.image('rock', 'assets/Rock.png');
        this.load.image('paper', 'assets/Paper.png');
        this.load.image('scissors', 'assets/Scissors.png');
    }

    create() {
        // Black background fill
        this.add.rectangle(235, 325, 470, 650, 0x000000);

        // Background image - center at (100, 200), scaled 0.75
        const bgImage = this.add.image(100, 200, 'background');
        bgImage.setScale(0.75);

        // Game State
        this.gameState = {
            playerChoice: null,
            computerChoice: null,
            playerScore: 0,
            gameOver: false,
            roundComplete: false
        };

        // Text at top - "Select your option" at (190, 190)
        this.selectText = this.add.text(190, 190, 'Select your option', {
            fontSize: '15px',
            fill: '#ffffff',
            backgroundColor: '#000000',
            padding: { x: 2, y: 2 }
        }).setOrigin(0.5, 0.5);

        // Create Choice Buttons at exact positions - Rock (80,80), Paper (230,80), Scissors (370,80)
        this.rockButton = this.add.image(80, 80, 'rock')
            .setScale(0.5)
            .setOrigin(0.5, 0.5)
            .setInteractive({ useHandCursor: true });
        this.rockButton.on('pointerdown', () => this.playerSelect(0));

        this.paperButton = this.add.image(230, 80, 'paper')
            .setScale(0.5)
            .setOrigin(0.5, 0.5)
            .setInteractive({ useHandCursor: true });
        this.paperButton.on('pointerdown', () => this.playerSelect(1));

        this.scissorsButton = this.add.image(370, 80, 'scissors')
            .setScale(0.5)
            .setOrigin(0.5, 0.5)
            .setInteractive({ useHandCursor: true });
        this.scissorsButton.on('pointerdown', () => this.playerSelect(2));

        // Player choice display - rect at (80, 250, 50, 50)
        this.playerChoiceImg = null;

        // Computer choice display - rect at (270, 250, 50, 50)
        this.computerChoiceImg = null;

        // Result text at (235, 425) - 0.5 * width
        this.resultText = this.add.text(235, 425, 'Result', {
            fontSize: '30px',
            fill: '#ffffff'
        }).setOrigin(0.5, 0.5);

        // Score text at (235, 585) - 0.5 * width, 0.9 * height
        this.scoreText = this.add.text(235, 585, 'Score : 0 / 3', {
            fontSize: '30px',
            fill: '#ffffff'
        }).setOrigin(0.5, 0.5);

        // Reset Button text - visible only after round completes
        this.resetButtonText = this.add.text(235, 425, 'Click on the button to reset the game', {
            fontSize: '20px',
            fill: '#ffffff'
        }).setOrigin(0.5, 0.5);
        this.resetButtonText.setVisible(false);

        this.resetButton = this.add.text(235, 475, 'Button', {
            fontSize: '20px',
            fill: '#000000',
            backgroundColor: '#cccccc',
            padding: { x: 10, y: 5 }
        }).setOrigin(0.5, 0.5)
            .setInteractive({ useHandCursor: true });
        this.resetButton.on('pointerdown', () => this.resetRound());
        this.resetButton.setVisible(false);
    }

    playerSelect(choiceIndex) {
        // Only allow selection if game is not over
        if (this.gameState.gameOver) return;

        this.gameState.playerChoice = choiceIndex;

        // Display player choice at (80, 250)
        if (this.playerChoiceImg) this.playerChoiceImg.destroy();
        
        const choiceKey = choiceIndex === 0 ? 'rock' : (choiceIndex === 1 ? 'paper' : 'scissors');
        this.playerChoiceImg = this.add.image(80, 250, choiceKey);
        this.playerChoiceImg.setScale(0.5).setOrigin(0.5, 0.5);

        // Computer selection with delay
        this.time.delayedCall(500, () => {
            this.computerSelect();
        });
    }

    computerSelect() {
        this.gameState.computerChoice = Phaser.Math.Between(0, 2);

        // Display computer choice at (270, 250)
        if (this.computerChoiceImg) this.computerChoiceImg.destroy();
        
        const choiceKey = this.gameState.computerChoice === 0 ? 'rock' : (this.gameState.computerChoice === 1 ? 'paper' : 'scissors');
        this.computerChoiceImg = this.add.image(270, 250, choiceKey);
        this.computerChoiceImg.setScale(0.5).setOrigin(0.5, 0.5);

        // Determine winner with delay
        this.time.delayedCall(500, () => {
            this.determineWinner();
        });
    }

    determineWinner() {
        const player = this.gameState.playerChoice;
        const computer = this.gameState.computerChoice;
        let resultMsg = '';

        if (player === computer) {
            resultMsg = 'YOU TIE';
        } else if (
            (player === 0 && computer === 2) ||  // Rock beats Scissors
            (player === 1 && computer === 0) ||  // Paper beats Rock
            (player === 2 && computer === 1)     // Scissors beats Paper
        ) {
            resultMsg = 'Hurrehhh, YOU WON!!!';
            this.gameState.playerScore++;
        } else {
            resultMsg = 'COMPUTER GOT YA';
        }

        // Update result display
        this.resultText.setText(resultMsg);

        // Update score display
        this.scoreText.setText(`Score : ${this.gameState.playerScore} / 3`);

        // Mark round as complete
        this.gameState.roundComplete = true;

        // Check if player reached 3 wins (game over)
        if (this.gameState.playerScore === 3) {
            this.gameOver();
        } else {
            // Show reset button for next round
            this.showResetButton();
        }
    }

    determineWinner() {
        const player = this.gameState.playerChoice;
        const computer = this.gameState.computerChoice;
        let resultMsg = '';

        if (player === computer) {
            resultMsg = 'YOU TIE';
        } else if (
            (player === 0 && computer === 2) ||  // Rock beats Scissors
            (player === 1 && computer === 0) ||  // Paper beats Rock
            (player === 2 && computer === 1)     // Scissors beats Paper
        ) {
            resultMsg = 'Hurrehhh, YOU WON!!!';
            this.gameState.playerScore++;
        } else {
            resultMsg = 'COMPUTER GOT YA';
        }

        // Update result display
        this.resultText.setText(resultMsg);

        // Update score display
        this.scoreText.setText(`Score : ${this.gameState.playerScore} / 3`);

        // Check if player reached 3 wins (game over)
        if (this.gameState.playerScore === 3) {
            this.gameOver();
        }
    }

    showResetButton() {
        this.resultText.setVisible(false);
        this.resetButtonText.setText('Click on the button to reset the game');
        this.resetButtonText.setVisible(true);
        this.resetButton.setVisible(true);
    }

    gameOver() {
        this.resultText.setText('GAME OVER!!!!!');
        this.gameState.gameOver = true;
        this.resetButtonText.setVisible(false);
        this.resetButton.setVisible(true);
    }

    resetRound() {
        // Full game reset - only called from game over
        this.gameState.playerChoice = null;
        this.gameState.computerChoice = null;
        this.gameState.playerScore = 0;
        this.gameState.gameOver = false;
        this.gameState.roundComplete = false;
        
        // Clear displayed images
        if (this.playerChoiceImg) this.playerChoiceImg.destroy();
        if (this.computerChoiceImg) this.computerChoiceImg.destroy();
        this.playerChoiceImg = null;
        this.computerChoiceImg = null;
        
        // Reset displays
        this.resultText.setText('Result');
        this.resultText.setVisible(true);
        this.scoreText.setText('Score : 0 / 3');
        
        // Hide reset buttons
        this.resetButtonText.setVisible(false);
        this.resetButton.setVisible(false);
    }
}

// Game Configuration
const config = {
    type: Phaser.AUTO,
    parent: 'game-container',
    width: 470,
    height: 650,
    backgroundColor: '#000000',
    scene: RockPaperScissorsScene,
    render: {
        pixelArt: false,
        antialias: true,
        smoothProperty: true
    }
};

const game = new Phaser.Game(config);
