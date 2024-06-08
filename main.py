@namespace
class SpriteKind:
    Weapon = SpriteKind.create()
game.splash("Fortnite: 2D")
mySprite = sprites.create(assets.image("""
    Jonesy
"""), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_scale(2, ScaleAnchor.MIDDLE)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
scene.camera_follow_sprite(mySprite)
EditPaper = sprites.create(assets.image("""
    EditPaper
"""), SpriteKind.Weapon)
sprites.destroy(EditPaper)
Shoty = sprites.create(assets.image("""
    Shoty
"""), SpriteKind.Weapon)
Shoty.set_scale(2, ScaleAnchor.MIDDLE)
Shoty.follow(mySprite, 500)

def on_on_update():
    global EditPaper, Shoty
    if Shoty.overlaps_with(mySprite):
        if controller.up.is_pressed():
            mySprite.set_image(assets.image("""
                Jonesy Backside
            """))
            Shoty.set_image(assets.image("""
                Shoty
            """))
        if controller.right.is_pressed():
            mySprite.set_image(assets.image("""
                Jonesy Right Side
            """))
            Shoty.set_image(assets.image("""
                Shoty
            """))
        if controller.left.is_pressed():
            mySprite.set_image(assets.image("""
                Jonesy Left Side
            """))
            Shoty.set_image(assets.image("""
                ShotyAlt
            """))
        if controller.down.is_pressed():
            mySprite.set_image(assets.image("""
                Jonesy
            """))
            Shoty.set_image(assets.image("""
                Shoty
            """))
        if controller.B.is_pressed():
            sprites.destroy(Shoty)
            sprites.destroy(EditPaper)
            EditPaper = sprites.create(assets.image("""
                EditPaper
            """), SpriteKind.Weapon)
            EditPaper.set_scale(2, ScaleAnchor.MIDDLE)
            EditPaper.follow(mySprite, 500)
    else:
        if EditPaper.overlaps_with(mySprite):
            if controller.up.is_pressed():
                mySprite.set_image(assets.image("""
                    Jonesy Backside
                """))
                EditPaper.set_image(assets.image("""
                    EditPaper
                """))
            if controller.right.is_pressed():
                mySprite.set_image(assets.image("""
                    Jonesy Right Side
                """))
                EditPaper.set_image(assets.image("""
                    EditPaper
                """))
            if controller.left.is_pressed():
                mySprite.set_image(assets.image("""
                    Jonesy Left Side
                """))
                EditPaper.set_image(assets.image("""
                    EditPaperAlt
                """))
            if controller.down.is_pressed():
                mySprite.set_image(assets.image("""
                    Jonesy
                """))
                EditPaper.set_image(assets.image("""
                    EditPaper
                """))
            if controller.B.is_pressed():
                sprites.destroy(Shoty)
                sprites.destroy(EditPaper)
                Shoty = sprites.create(assets.image("""
                    Shoty
                """), SpriteKind.Weapon)
                Shoty.set_scale(2, ScaleAnchor.MIDDLE)
                Shoty.follow(mySprite, 500)
game.on_update(on_on_update)
