 // Get all legal moves for a piece at (row,col) (filter out moves that leave king in check)
            function getValidMoves(row, col) {
                const piece = gameState.board[row][col];
                if (!piece || piece.color !== gameState.currentPlayer) return [];

                let possible = [];
                switch (piece.type) {
                    case 'pawn': possible = getPawnMoves(row, col, piece.color); break;
                    case 'knight': possible = getKnightMoves(row, col, piece.color); break;
                    case 'bishop': possible = getBishopMoves(row, col, piece.color); break;
                    case 'rook': possible = getRookMoves(row, col, piece.color); break;
                    case 'queen': possible = getQueenMoves(row, col, piece.color); break;
                    case 'king': possible = getKingMoves(row, col, piece.color); break;
                }

                const valid = [];
                for (const m of possible) {
                    const testBoard = JSON.parse(JSON.stringify(gameState.board));
                    applyTestMove(testBoard, row, col, m.row, m.col, piece, m.type);
                    // Find king position
                    let kingPos = null;
                    for (let r = 0; r < 8; r++) {
                        for (let c = 0; c < 8; c++) {
                            const p = testBoard[r][c];
                            if (p && p.type === 'king' && p.color === piece.color) {
                                kingPos = { row: r, col: c };
                                break;
                            }
                        }
                        if (kingPos) break;
                    }
                    if (kingPos && !isSquareAttacked(piece.color, kingPos.row, kingPos.col, testBoard)) {
                        valid.push(m);
                    }
                }
                return valid;
            }

            // ---------- Evaluation (uses learningParams) ----------
            function evaluateBoard() {
                let score = 0;
                let totalPieces = 0;
                for (let r = 0; r < 8; r++) {
                    for (let c = 0; c < 8; c++) {
                        if (gameState.board[r][c]) totalPieces++;
                    }
                }
                const isEndgame = totalPieces <= 10;

                for (let r = 0; r < 8; r++) {
                    for (let c = 0; c < 8; c++) {
                        const piece = gameState.board[r][c];
                        if (!piece) continue;

                        const val = learningParams.pieceValues[piece.type];
                        let pos = 0;
                        if (piece.type === 'pawn') {
                            pos = piece.color === 'white' ? learningParams.pawnTable[r][c] : -learningParams.pawnTable[7 - r][c];
                        } else if (piece.type === 'knight') {
                            pos = piece.color === 'white' ? learningParams.knightTable[r][c] : -learningParams.knightTable[7 - r][c];
                        } else if (piece.type === 'bishop') {
                            pos = piece.color === 'white' ? learningParams.bishopTable[r][c] : -learningParams.bishopTable[7 - r][c];
                        } else if (piece.type === 'rook') {
                            pos = piece.color === 'white' ? learningParams.rookTable[r][c] : -learningParams.rookTable[7 - r][c];
                        } else if (piece.type === 'queen') {
                            pos = piece.color === 'white' ? learningParams.queenTable[r][c] : -learningParams.queenTable[7 - r][c];
                        } else if (piece.type === 'king') {
                            const table = isEndgame ? learningParams.kingEndgameTable : learningParams.kingMiddleTable;
                            pos = piece.color === 'white' ? table[r][c] : -table[7 - r][c];
                        }

                        if (piece.color === 'white') score += val + pos;
                        else score -= val + pos;
                    }
                }
                return score;
            }

            // ---------- AI Move Selection (minimax with depth 3) ----------
            function getAllValidMoves(color) {
                const moves = [];
                for (let r = 0; r < 8; r++) {
                    for (let c = 0; c < 8; c++) {
                        const piece = gameState.board[r][c];
                        if (piece && piece.color === color) {
                            const pieceMoves = getValidMoves(r, c);
                            for (const m of pieceMoves) {
                                moves.push({ from: { row: r, col: c }, to: { row: m.row, col: m.col }, type: m.type });
                            }
                        }
                    }
                }
                return moves;
            }

            function minimax(depth, alpha, beta, isMaximizing) {
                if (depth === 0) return { score: evaluateBoard(), move: null };

                const color = isMaximizing ? 'white' : 'black';
                const allMoves = getAllValidMoves(color);
                if (allMoves.length === 0) {
                    if (isKingInCheck(color, gameState.board)) {
                        return { score: isMaximizing ? -Infinity : Infinity, move: null };
                    } else {
                        return { score: 0, move: null };
                    }
                }

                let bestMove = null;
                if (isMaximizing) {
                    let maxEval = -Infinity;
                    for (const move of allMoves) {
                        const boardCopy = JSON.parse(JSON.stringify(gameState.board));
                        const piece = boardCopy[move.from.row][move.from.col];
                        applyTestMove(boardCopy, move.from.row, move.from.col, move.to.row, move.to.col, piece, move.type);

                        const original = gameState.board;
                        gameState.board = boardCopy;
                        const evalResult = minimax(depth - 1, alpha, beta, false).score;
                        gameState.board = original;

                        if (evalResult > maxEval) {
                            maxEval = evalResult;
                            bestMove = move;
                        }
                        alpha = Math.max(alpha, evalResult);
                        if (beta <= alpha) break;
                    }
                    return { score: maxEval, move: bestMove };
                } else {
                    let minEval = Infinity;
                    for (const move of allMoves) {
                        const boardCopy = JSON.parse(JSON.stringify(gameState.board));
                        const piece = boardCopy[move.from.row][move.from.col];
                        applyTestMove(boardCopy, move.from.row, move.from.col, move.to.row, move.to.col, piece, move.type);

                        const original = gameState.board;
                        gameState.board = boardCopy;
                        const evalResult = minimax(depth - 1, alpha, beta, true).score;
                        gameState.board = original;

                        if (evalResult < minEval) {
                            minEval = evalResult;
                            bestMove = move;
                        }
                        beta = Math.min(beta, evalResult);
                        if (beta <= alpha) break;
                    }
                    return { score: minEval, move: bestMove };
                }
            }

            function getAIMove() {
                const allMoves = getAllValidMoves('black');
                if (allMoves.length === 0) return null;
                const best = minimax(3, -Infinity, Infinity, false); // AI is black (minimizing)
                return best.move;
            }

            // ---------- Make Move (real move) ----------
            function makeMove(from, to, moveType, promotionPiece = 'queen') {
                const piece = gameState.board[from.row][from.col];
                const targetPiece = gameState.board[to.row][to.col];

                // Record position for learning (before move)
                const boardCopy = JSON.parse(JSON.stringify(gameState.board));
                const evalBefore = evaluateBoard();
                gameState.gamePositions.push({
                    board: boardCopy,
                    eval: evalBefore,
                    move: { from, to, type: moveType },
                    player: gameState.currentPlayer
                });

                // Handle special moves
                if (moveType === 'enPassant') {
                    const capturedRow = piece.color === 'white' ? to.row + 1 : to.row - 1;
                    const captured = gameState.board[capturedRow][to.col];
                    gameState.capturedPieces[piece.color].push(captured.type);
                    gameState.board[capturedRow][to.col] = null;
                } else if (moveType === 'castle') {
                    if (to.col === 6) { // kingside
                        gameState.board[to.row][7] = null;
                        gameState.board[to.row][5] = { type: 'rook', color: piece.color, hasMoved: true };
                    } else if (to.col === 2) { // queenside
                        gameState.board[to.row][0] = null;
                        gameState.board[to.row][3] = { type: 'rook', color: piece.color, hasMoved: true };
                    }
                } else if (targetPiece && moveType === 'capture') {
                    gameState.capturedPieces[piece.color].push(targetPiece.type);
                }

                // Move piece
                const movedPiece = { ...piece, hasMoved: true };
                if (piece.type === 'pawn' && (to.row === 0 || to.row === 7)) {
                    movedPiece.type = promotionPiece;
                }
                gameState.board[to.row][to.col] = movedPiece;
                gameState.board[from.row][from.col] = null;

                // Update king position if king moved
                if (piece.type === 'king') {
                    gameState.kingPosition[piece.color] = { row: to.row, col: to.col };
                    gameState.canCastle[piece.color] = { kingSide: false, queenSide: false };
                }

                // Update castling rights if rook moved
                if (piece.type === 'rook') {
                    if (from.row === 0 && from.col === 0) gameState.canCastle.black.queenSide = false;
                    if (from.row === 0 && from.col === 7) gameState.canCastle.black.kingSide = false;
                    if (from.row === 7 && from.col === 0) gameState.canCastle.white.queenSide = false;
                    if (from.row === 7 && from.col === 7) gameState.canCastle.white.kingSide = false;
                }

                // Set en passant target
                gameState.enPassantTarget = null;
                if (moveType === 'doublePawn') {
                    gameState.enPassantTarget = {
                        row: piece.color === 'white' ? to.row + 1 : to.row - 1,
                        col: to.col
                    };
                }

                // Save move to history
                gameState.moveHistory.push({
                    from: { ...from },
                    to: { ...to },
                    piece: { ...piece },
                    capturedPiece: targetPiece ? { ...targetPiece } : null,
                    moveType,
                    promotionPiece: (piece.type === 'pawn' && (to.row === 0 || to.row === 7)) ? promotionPiece : null,
                    enPassantTargetBefore: gameState.enPassantTarget,
                    canCastleBefore: JSON.parse(JSON.stringify(gameState.canCastle)),
                    kingPositionBefore: JSON.parse(JSON.stringify(gameState.kingPosition))
                });

                // Switch player
                gameState.currentPlayer = gameState.currentPlayer === 'white' ? 'black' : 'white';

                // Update clocks
                if (piece.type === 'pawn' || moveType === 'capture') gameState.halfMoveClock = 0;
                else gameState.halfMoveClock++;

                if (gameState.currentPlayer === 'white') gameState.fullMoveNumber++;

                // Check game status
                checkGameStatus();

                // UI updates
                gameState.selectedSquare = null;
                gameState.validMoves = [];
                renderBoard();
                updateGameStatus();
                updateCapturedPieces();

                // If game over, trigger learning
                if (gameState.gameOver && gameState.gameResult) {
                    learnFromGame(gameState.gameResult);
                }

                // If AI enabled and it's now black's turn and game not over, schedule AI move
                if (!gameState.gameOver && gameState.aiEnabled && gameState.currentPlayer === 'black') {
                    gameState.aiThinking = true;
                    renderBoard();
                    setTimeout(() => {
                        const aiMove = getAIMove();
                        if (aiMove) {
                            const piece = gameState.board[aiMove.from.row][aiMove.from.col];
                            if (piece.type === 'pawn' && (aiMove.to.row === 0 || aiMove.to.row === 7)) {
                                makeMove(aiMove.from, aiMove.to, aiMove.type, 'queen');
                            } else {
                                makeMove(aiMove.from, aiMove.to, aiMove.type);
                            }
                        }
                        gameState.aiThinking = false;
                        renderBoard();
                    }, 500);
                }
            }

            // ---------- Game Over & Learning ----------
            function checkGameStatus() {
                const current = gameState.currentPlayer;
                gameState.check = isKingInCheck(current, gameState.board);

                // See if current player has any legal moves
                let hasLegal = false;
                for (let r = 0; r < 8 && !hasLegal; r++) {
                    for (let c = 0; c < 8 && !hasLegal; c++) {
                        const p = gameState.board[r][c];
                        if (p && p.color === current && getValidMoves(r, c).length > 0) hasLegal = true;
                    }
                }

                if (!hasLegal) {
                    if (gameState.check) {
                        gameState.checkmate = true;
                        gameState.gameOver = true;
                        gameState.gameResult = (current === 'white') ? 'ai_win' : 'ai_loss'; // black wins if white checkmated
                    } else {
                        gameState.gameOver = true;
                        gameState.gameResult = 'draw';
                    }
                } else {
                    gameState.checkmate = false;
                    gameState.gameOver = false;
                }
            }

            function learnFromGame(result) {
                if (gameState.gamePositions.length === 0) return;

                // Update stats
                learningStats.gamesPlayed++;
                if (result === 'ai_win') learningStats.aiWins++;
                else if (result === 'ai_loss') learningStats.playerWins++;
                else learningStats.draws++;
                updateStatsDisplay();

                const learningRate = 0.01;
                // Determine target: +10000 for win, -10000 for loss, 0 for draw
                const target = result === 'ai_win' ? 10000 : (result === 'ai_loss' ? -10000 : 0);

                // Iterate through recorded positions (reverse order, recent more important)
                for (let i = gameState.gamePositions.length - 1; i >= 0; i--) {
                    const pos = gameState.gamePositions[i];
                    // Temporarily set board to this position
                    const originalBoard = gameState.board;
                    gameState.board = pos.board;
                    const currentEval = evaluateBoard();
                    gameState.board = originalBoard;

                    const error = target - currentEval;

                    // Update piece values and tables based on this position's pieces
                    for (let r = 0; r < 8; r++) {
                        for (let c = 0; c < 8; c++) {
                            const piece = pos.board[r][c];
                            if (!piece) continue;

                            const sign = (piece.color === 'white') ? 1 : -1;
                            // Update base piece value
                            learningParams.pieceValues[piece.type] += learningRate * error * sign * 0.01; // small multiplier

                            // Update piece-square table
                            let table = null;
                            switch (piece.type) {
                                case 'pawn': table = learningParams.pawnTable; break;
                                case 'knight': table = learningParams.knightTable; break;
                                case 'bishop': table = learningParams.bishopTable; break;
                                case 'rook': table = learningParams.rookTable; break;
                                case 'queen': table = learningParams.queenTable; break;
                                case 'king': table = learningParams.kingMiddleTable; break; // simplified
                            }
                            if (table) {
                                const rowIdx = piece.color === 'white' ? r : 7 - r;
                                table[rowIdx][c] += learningRate * error * sign * 0.1;
                            }
                        }
                    }
                }

                // Save after learning
                saveBrain();
            }
