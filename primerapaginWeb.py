<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello world!</title>
    <meta charset="wtf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link
      href="https://fonts.googleapis.com/css2?family=Sansita&display=swap"
      rel="stylesheet"
    />

    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />

    <link rel="stylesheet" href="/style.css" />
  </head>
  <body>
    <header>
      <link
        href="https://fonts.googleapis.com/css2?family=Allerta&family=Sansita:ital,wght@1,900&display=swap"
        rel="stylesheet"
      />
      <nav class="navbar navbar-expand-lg navbar-light">
        <a class="navbar-brand" href="#">Logo</a>

        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link" href="#">Inicio <span> </span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Galería</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Acerca de</a>
          </li>
        </ul>
      </nav>

      <!--TITULO-->

      <div
        class="cover d-flex justify-content-center align-items-center flex-column"
      >
        <h1>La Reserva</h1>
        <p>Explosión de creatividad artesanal</p>
        <button class="btn btn-warning">Conoce más</button>
      </div>
    </header>

    <!--TARJETAS-->

    <section>
      <div class="container mt-5 mb-5">
        <div class="row">
          <div class="col-12 col-sm-6 col-md-4 col-lg-4 mt-2">
            <!--TARJETA 1-->

            <div class="card">
              <div
                title="Manos tallando madera"
                class="cover cover-small"
                style="
                  background-image: url(https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/rsz_talla_de_madera.jpg?v=1655659338669);
                "
              ></div>

              <div class="card-body">
                <h5 class="card-title">Artesanía</h5>
                <p class="card-text">
                  Trabajos realizados a mano, siguiendo procesos tradicionales .
                  El disfrute de los elementos.
                </p>
              </div>
            </div>
          </div>

          <div class="col-12 col-sm-6 col-md-4 col-lg-4 mt-2">
            <!--TARJETA 2-->

            <div class="card">
              <div
                title="Bloques de madera de colores"
                class="cover cover-small"
                style="
                  background-image: url(https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/dise%C3%B1o%20abstracto%20maderas.jpg?v=1655592655956);
                "
              ></div>
              <div class="card-body">
                <h5 class="card-title">Arte Digital</h5>
                <p class="card-text">
                  Fotografía, diseño y proyectos realizados en familia Adobe,
                  Cinema 4, Blender, Maya, Mudbox.
                </p>
              </div>
            </div>
          </div>

          <div class="col-12 col-sm-6 col-md-4 col-lg-4 mt-2">
            <!--TARJETA 3-->

            <div class="card">
              <div
                title="Persona haciendo boceto"
                class="cover cover-small"
                style="
                  background-image: url(https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/bocetos.jpg?v=1655592773867);
                "
              ></div>
              <div class="card-body">
                <h5 class="card-title">Bocetos</h5>
                <p class="card-text">
                  Ideas y bocetos para proyectos futuros de todo tipo, forma y
                  dificultad. El arte de la mente abierta.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!--DIBUJO Y TEXTO-->
    <section>
      <div class="container mt-5 mb-5">
        <div class="row">
          <div class="row justify-content-center align-items-center minh-30">
            <div class="col-12 col-sm-9 col-lg-12">
              <img
                src="https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/en%20equipo.svg?v=1655747272720"
                alt="persona levantado dedo enviando datos"
                class="rounded float-start"
                width="43%"
                height="60%"
              />
              <img
                src="https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/Unirse.svg?v=1655774547924"
                alt="persona levantado dedo enviando datos"
                class="rounded float-start"
                width="50%"
                height="60%"
              />

              <div class="col-12 col-sm-9">
                <h3>¡ Inspiranos con tus comentarios !</h3>
                <p>
                  Mandanos las ideas que busques ver realizadas y daremos
                  nuestros mejores consejos, dando uso a todos nuestros
                  conocimientos. No dudes en preguntar, estaremos muy
                  satisfechos de ver vuestros propios trabajos cojer forma y
                  desarrollarse, con solo un pequeño impulso. ¡¡No hay nada que
                  te frene, salvo tu propia imaginación!!
                </p>
              </div>
              <a href="#">Soluciones y respuestas</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- EMAIL -->
    <section>
      <div class="container mt-5 mb-5">
        <form class="row gy-2 gx-3 align-items-center">
          <div class="col-auto">
            <label class="visually-hidden" for="autoSizingInput">Nombre</label>
            <input
              type="text"
              class="form-control"
              id="autoSizingInput"
              placeholder="Nombre"
            />
          </div>
          <div class="col-auto">
            <label class="visually-hidden" for="autoSizingInputGroup"
              >Usuario</label
            >
            <div class="input-group">
              <div class="input-group-text">@</div>
              <input
                type="text"
                class="form-control"
                id="autoSizingInputGroup"
                placeholder="Email"
              />
            </div>
          </div>
          <div class="col-auto">
            <label class="visually-hidden" for="autoSizingSelect"
              >Preference</label
            >
            <select class="form-select" id="autoSizingSelect">
              <option selected>Sección</option>
              <option value="1">Maderas</option>
              <option value="2">Arte Digital</option>
              <option value="3">Fotografía</option>
            </select>
          </div>
          <div class="col-auto">
            <div class="form-check">
              <input
                class="form-check-input"
                type="checkbox"
                id="autoSizingCheck"
              />
              <label class="form-check-label" for="autoSizingCheck">
                Recordar
              </label>
            </div>
          </div>
          <div class="col-auto">
            <button type="submit" class="btn btn-primary">Enviar</button>
          </div>
        </form>
      </div>
    </section>
    <section>
      <div class="text-bg-info p-3">Info with contrasting color</div>
      <div class="text-bg-info p-3">
         </div>
      <span class="badge text-bg-info">Info</span>
      
      <!--TIRA DE GALERIA ARTESANAL-->
      <div class="container mt-5 mb-5">
        <div id="carousel-caption" class="carousel slide" data-bs-ride="false">
          <div class="carousel-indicators">
            <button
              type="button"
              data-bs-target="carousel-caption"
              data-bs-slide-to="0"
              class="active"
              aria-current="true"
              aria-label="Slide 1"
            ></button>
            <button
              type="button"
              data-bs-target="carousel-caption"
              data-bs-slide-to="1"
              aria-label="Slide 2"
            ></button>
            <button
              type="button"
              data-bs-target="carousel-caption"
              data-bs-slide-to="2"
              aria-label="Slide 3"
            ></button>
            <button
              type="button"
              data-bs-target="carousel-caption"
              data-bs-slide-to="3"
              aria-label="Slide 4"
            ></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img
                src="https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/buriles%20para%20madera%C3%A7.jpg?v=1655753053518"
                class="d-block w-100"
                alt="buriles para madera"
              />
              <div class="carousel-caption d-none d-md-block">
                <h5>*La Astillita</h5>
                
                <p>
                  Some representative placeholder content for the first slide.
                </p>
              </div>
            </div>
            <div class="carousel-item">
              <img
                src="https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/lapicero%20con%20lapices.jpg?v=1655753053518"
                class="d-block w-100"
                alt="lapicero con colores de madera"
              />
              <div class="carousel-caption d-none d-md-block">
                <h5>* El Sacapuntas</h5>
                <p>
                  Some representative placeholder content for the second slide.
                </p>
              </div>
            </div>
            <div class="carousel-item">
              <img
                src="https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/escritorio%20volante.jpg?v=1655753053518"
                class="d-block w-100"
                alt="atril de carton con portatil encima"
              />
              <div class="carousel-caption d-none d-md-block">
                <h5>* El Tornillo</h5>
                <p>
                  Some representative placeholder content for the third slide.
                </p>
              </div>
            </div>
            <div class="carousel-item">
              <img
                src="https://cdn.glitch.global/2997c26d-ea4b-477b-8793-ff2e0f94c670/guitarrista%20zoom.jpg?v=1655753053518"
                class="d-block w-100"
                alt="atril de carton con portatil encima"
              />
              <div class="carousel-caption d-none d-md-block">
                <h5>* El Objetivo</h5>
                <p>
                  Some representative placeholder content for the third slide.
                </p>
              </div>
            </div>
          </div>
          <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="carousel-caption"
            data-bs-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            data-bs-target="carousel-caption"
            data-bs-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
      
      
    <!-- PRUEBA-->
      
      
      
      
      
      
      
      
      
      
      
      
      
    </section>
  </body>
</html>
