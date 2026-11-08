<?php 

  $title = "Daftar Produk";

  $products = [
    [
      "nama" => "Dimsum",
      "harga" => 10_000,
      "gambar"=> "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4k5ldzLXVTHhuT34JW97xzUppLwcG0JtoFiGmMzRjCA&s=10",
      "stok" => 5,
    ],
    [
      "nama" => "Seblak",
      "harga" => 12_000,
      "gambar" => "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHT1FquY0gHE0tgxXDTdob0KdGtvrBnUHebDyRocvuUQ&s=10",
      "stok" => 3,
    ],
    [
      "nama" => "Es Teh Manis",
      "harga" => 50_000,
      "gambar" => "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLnikV8Z5jg8qhZfWpk2m0ofZX5bZG6j-NQCkg7EBUIg&s=10",
      "stok" => 0,
    ],
    [
      "nama" => "Es Teh Manis Panas",
      "harga" => 50_000,
      "gambar" => "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEz7V-2pKoz8AwUepZ9r2DLhA7UzgZVKEoH0bYcTztXw&s=10",
      "stok" => 2,
    ],
  ];

?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title> <?= $title ?> </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  </head>

  <body>

    <div class="container mt-4 row">

      <?php foreach($products as $p) : ?>

        <div class="col-12 col-lg-3 col-md-4">
          <div class="card">

            <img src="<?= $p['gambar'] ?>" 
                 class="card-img-top" 
                 alt="<?= $p['nama'] ?>">

            <div class="card-body">

              <h5 class="card-title"> <?= $p['nama'] ?></h5>

              <p class="card-text"> <?= $p['harga'] ?></p>

              <p class="card-text">Stok: <?= $p['stok'] ?></p>

              <?php if ($p['stok'] > 0) : ?>

                <a href="#" 
                   class="btn btn-primary"
                   onclick="alert('<?= $p['nama'] ?> sudah ditambahkan ke keranjang!'); return false;">
                  Tambah ke Keranjang
                </a>

              <?php else : ?>

                <a href="#" 
                   class="btn btn-primary"
                   onclick="alert('Stok <?= $p['nama'] ?> habis!'); return false;">
                  Tambah ke Keranjang
                </a>

              <?php endif; ?>

            </div>
          </div>
        </div>

      <?php endforeach; ?>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>

  </body>
</html>